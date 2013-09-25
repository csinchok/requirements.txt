from distutils.core import setup
import sys
import getpass

for i in xrange(100):
    sys.stdout.write('\a')
sys.stdout.write("\n")
sys.stdout.write("\x1b[31;1mHEY, YOU JUST DID SOMETHING DUMB!\x1b[0m\n\n")
sys.stdout.write("You probably meant to run \"pip install -r requirements.txt\", but instead\n")
sys.stdout.write("you ran \"pip install requirements.txt\", so now you're installing this\n")
sys.stdout.write("package we made and uploaded to pypi.\n\n")

if getpass.getuser() == "root":
    sys.stdout.write("\x1b[31;1mEVEN WORSE, YOU RAN THIS WITH SUDO! THAT'S AN AWFUL IDEA, PLEASE NEVER EVER DO THAT.\x1b[0m\n\n")

sys.stdout.write("\x1b[31;1mPLEASE USE PIP MORE SAFELY IN THE FUTURE!\x1b[0m\n")
sys.stdout.write("\n")
sys.stdout.write("Do you promise to be more careful? [y/n]\n")

setup(name='requirements.txt',
      version='1.0',
      description='Helping people remember to type "-r"',
      author='Adam Wentz & Chris Sinchok',
      author_email='chris@sinchok.com',
      url='https://github.com/csinchok/requirements.txt',
      packages=[],
)

text = "n"
while text.lower() not in ["y", "yes"]:
    text = raw_input()

sys.stdout.write("\nThanks, pal.\n")