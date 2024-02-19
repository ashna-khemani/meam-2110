import zipfile
import os
import sys
import shutil
import traceback

def EvaluateProblem(problem, output_file):
  '''
  To generate human-gradeable results:
  1) copy the script to the results text file
  2) Pipe stdout to the file
  3) Execute the script
  '''
  orig = sys.stdout
  shutil.copyfile(problem, output_file)
  with open(output_file, "a") as f:
    
    error = None
    sys.stdout = f
    try:
      exec(open(problem).read())
    except Exception as e:
      error = traceback.format_exc()
      print(error)
    finally:
      sys.stdout = orig

    if error is not None:
      print('\nUh oh! Your textbook problem ' + problem + ' encountered an error while running. ' + 
            'The submission .zip file has been created, and can be submitted to the autograder, ' + 
            'but the textbook problem will need to be fixed for full credit. The error message is below.\n\n')
      print(error)

problem617 = os.path.join("assignments", "project2", "problem_6_17.py")
output617 = os.path.join("assignments", "project2", "problem_6_17_result.txt")
EvaluateProblem(problem617, output617)

problem619 = os.path.join("assignments", "project2", "problem_6_19.py")
output619 = os.path.join("assignments", "project2", "problem_6_19_result.txt")
EvaluateProblem(problem619, output619)


'''
Create a zip archive with all the .py files in meam2110/
Add in generated output files from textbook problems
'''
with zipfile.ZipFile(os.path.join(os.getcwd(), "assignments", "project2_submission.zip"), mode="w") as archive:
  archive.write(output617)
  archive.write(output619)
  for file in os.listdir('meam2110'):
    if file.endswith(".py"):
      archive.write(os.path.join("meam2110", file))
  archive.close()