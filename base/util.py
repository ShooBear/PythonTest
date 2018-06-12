import os
import yaml
import tempfile
import cPickle
import subprocess
import re
import operator

CRED = '\033[91m'
CEND = '\033[0m'


def is_genie_running():
    if os.path.exists(RUNNING_GENIE_FLAG_FILE):
        return True
    else:
        return False


def subprocess_open(command):
    popen = subprocess.Popen(command, stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE, shell=True)
    (stdoutdata, stderrdata) = popen.communicate()
    return stdoutdata, stderrdata


def delete_file(path):
    if os.path.exists(path):
        os.remove(path)


def remove_all_without_alpha_number(s):
    str = re.sub('[^0-9a-zA-Z]', '', s)
    return str


def yaml_dump(filepath, data):
    with open(filepath, 'w') as outfile:
        yaml.dump(data, outfile, default_flow_style=False)


def read_file(path):
    with open(path) as f:
        data = f.readlines()
    return data


def check_and_turn_to_red(string):
    if len(string) == 0:
        ret = CRED + 'Empty' + CEND
        return ret.encode('utf-8')
    else:
        return string.encode('utf-8')


def turn_to_red(string):
    return CRED + string + CEND


def get_file_dir():
    return os.path.dirname(os.path.realpath(__file__))


def load_yaml_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = yaml.load(f)
            return data


def store_file(filename, data=None, type='text', mode=644):
    dirname = os.path.abspath(os.path.dirname(filename))
    fd, temppath = tempfile.mkstemp(dir=dirname)
    with os.fdopen(fd, 'w') as f:
        if type == 'pickle':
            cPickle.dump(data, f, cPickle.HIGHEST_PROTOCOL)
        elif data is not None:
            f.write(data)

    os.chmod(temppath, mode)
    os.rename(temppath, filename)


def find_git_tag(git_dir, tag):
    tag_cmd = "git tag"
    amss_dir = git_dir + "amss"
    os.chdir(amss_dir)
    result = subprocess.check_output(tag_cmd, shell=True)
    tag_list = result.split('\n')
    if tag in tag_list:
        return True
    else:
        return False


def is_version(string):
    p = re.compile(".*v[\d]+\.[\d]+\.[\d]+\.[\d]+\.[\d]")
    if p.match(string) is not None:
        return True
    else:
        return False


def get_version(string):
    p = re.compile(".*v[\d]+\.[\d]+\.[\d]+\.[\d]+\.[\d]+-rc[0-9]*")
    match = p.match(string)
    if match is not None:
        return match.group()
    else:
        return None


def exec_command_get_result(cmd):
    process = os.popen(cmd)
    preprocessed = process.read()
    process.close()
    return preprocessed.split('\n')


def get_merged_version_list(from_ver, to_ver):
    cmd = 'git log {}..{} --merges --pretty=format:"%s"'.format(from_ver,
                                                                to_ver)
    ret = exec_command_get_result(cmd)
    merged_list = []
    for i in ret:
        i_split = i.split("'")
        if len(i_split) < 2:
            continue
        if is_version(i_split[1]):
            ver = i_split[1][i_split[1].find('v'):]
            merged_list.append(ver)
    return merged_list


def get_ret_dir_list():
    conf_filepath = get_file_dir() + '/config.yaml'
    conf = load_yaml_data(conf_filepath)
    dir_list = []
    for root, dirs, files in os.walk(conf['ret_dir']):
        for dir in dirs:
            if dir.startswith('v'):
                dir_list.append(dir)

    _dir_list = list(map(lambda dir: conf['ret_dir'] + '/' + dir, dir_list))
    return _dir_list


def sort_dict_by_key(dic):
    return sorted(dic.iteritems(), key=operator.itemgetter(0))


def get_reverted_hash(rvt_commit):
    revert_str = 'This reverts commit'
    _rhash = rvt_commit[rvt_commit.find(revert_str) + len(revert_str):]
    comma_index = _rhash.find('.')
    rhash = _rhash[:comma_index].strip()
    return rhash


def get_commit_info_from_str(commit, repo, type):
    info = commit.split(':')
    commit_hash = info[0]
    commiter = info[1]
    comment = ':'.join(info[2:])

    if type in ['revert', 'etc']:
        c_id = type
        content = comment
    else:
        c_id = comment[comment.find('#') + 1:].split()[0]
        content = comment[(comment.find(c_id)+len(c_id)):].strip()

    dic = {
        'commiter': commiter,
        'id': c_id,
        'content': content,
        'repo': repo,
        'iss_status': '',
        'hash': commit_hash,
        'reverted': '',
    }
    return dic


def get_commit_id_list_without_revert(commit_info):
    right_commit_id_list = list()
    for id, commits in commit_info.iteritems():
        for commit in commits:
            if commit['reverted'] != 'Reverted' \
                    and commit['id'] not in ['revert', 'etc']:
                right_commit_id_list.append(commit['id'])
    return right_commit_id_list
