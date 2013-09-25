from distutils.core import setup
import sys

sys.stdout.write("\n")
sys.stdout.write("\x1b[31;1mHEY, YOU JUST DID SOMETHING DUMB!\x1b[0m\n\n")
sys.stdout.write("You probably meant to run \"pip install -r requirements.txt\", but instead\n")
sys.stdout.write("you ran \"pip install requirements.txt\", so now you're installing this\n")
sys.stdout.write("package we made and uploaded to pypi.\n\n")
sys.stdout.write("\x1b[31;1mPLEASE USE PIP MORE SAFELY IN THE FUTURE!\x1b[0m\n")


setup(name='requirements.txt',
      version='1.0',
      description='Helping people remember to type "-r"',
      author='Adam Wentz & Chris Sinchok',
      author_email='tech@theonion.com',
      url='http://www.theonion.com',
      packages=[],
)