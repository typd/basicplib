from fabric.api import sudo, run, cd, env

lib_name = "basicplib"
git_url = "https://github.com/typd/basicplib"

def install():
    if not env.host_string:
        env.host_string = raw_input("host: ")
        env.user = raw_input("user: ")
    print "installing %s on %s:%s" % (lib_name, env.user, env.host_string)
    temp_dir = "tmp"
    if run("test -d %s" % temp_dir).failed:
        run("mkdir %s" % temp_dir)
    with cd(temp_dir):
        run("git clone %s" % git_url)
        with cd(lib_name):
            sudo("./install.sh")
    sudo("rm -rf %s" % temp_dir)

