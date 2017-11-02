import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_swapfile(File):
    f = File('/swapfile')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_swap(Command):
    output = Command("swapon -s | grep '/swapfile' | awk {'print $3'}").stdout

    assert '1048572' in output


def test_unmount_swap(Command):
    output = Command("swapoff /swapfile").stdout

    assert '' in output
