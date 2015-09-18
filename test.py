"""
Universal assignment tester
"""
 
import sys, os, re
import subprocess
import difflib

TIMEOUT = 10
assert len(sys.argv) == 2

def getstimulus(filename, directory):
  """
  Attempt to execute python module ```<directory>/stimulus/<filename>```, 
  capturing STDOUT and returning as a string.
  """
  try:
    stimproc = subprocess.Popen(['python3', directory + '/stimulus/' + filename, ''],
      universal_newlines=True, stdout = subprocess.PIPE, stderr=subprocess.STDOUT)
    return stimproc.communicate()[0]
  except:
    return ""

def testexemplar(filename, directory):
  """
  Attempt to execute python module ```<filename>```, passing it optional
  stimulus from the ```getstimulus``` function and comparing output with
  execution of python module ```<directory>/exemplars/<filename>```.
  """
  newlinetospace = lambda s: re.sub("[\r\n]+", " ", s)
  singlespace = lambda s: re.sub("[ \t]+", " ", s)
  stimulus = getstimulus(filename, directory)
  try:
    testproc = subprocess.Popen(['python3', filename,  ''], 
      universal_newlines=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    testout, err = testproc.communicate(input=stimulus, timeout=TIMEOUT)
    assert testproc.returncode == 0, testout
  except AssertionError:
    raise
  except subprocess.TimeoutExpired:
    testproc.kill()
    outs, errs = testproc.communicate()
    raise
  try:
    exemplar = directory + '/exemplars/' + filename
    if os.path.isfile(exemplar): 
      canproc = subprocess.Popen(['python3', exemplar, ''], 
        universal_newlines=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
      canout, err = canproc.communicate(input=stimulus, timeout=TIMEOUT)
      if canproc.returncode == 0:
        diffout = "Test case output does not match exemplar:\n"+''.join(difflib.unified_diff(canout.splitlines(), testout.splitlines(), 
          fromfile="exemplar", tofile="test case"))
        assert singlespace(newlinetospace(canout)) == singlespace(newlinetospace(testout)), diffout 
      else:
        raise RuntimeError(canout) 
  except subprocess.TimeoutExpired:
    canproc.kill()
    outs, errs = canproc.communicate()
    raise
  except AssertionError:
    raise
    
def testheader(filename):
  """
  Inspect ```<filename>``` for existence of a docstring header, looking
  for a filename match, and author string and credits.
  """
  with open(filename, 'r') as f:
    lines = f.readlines()
    assert lines[0].strip() in ['"""', "'''"], "Module must begin with a docstring header."
    assert lines[1].strip() == filename, "First line of docstring must be this file name."
    assert lines[2].lower().find('author:') == 0, "Second line of docstring must begin, 'Author: ...'"
    assert lines[2].find('<') == -1, "Second line of docstring must replace <..> with author name."
    assert lines[3].lower().find('credit:') == 0, "Third line of docstring must begin, 'Credit: ...'"
    assert lines[3].find('<') == -1, "Third line of docstring must replace <..> with sources or 'None'."

def test():
  filename = sys.argv[1]
  thisdir = os.path.dirname(__file__)
  testexemplar(filename, thisdir)
  testheader(filename)
  
if __name__ == '__main__':
    test()
