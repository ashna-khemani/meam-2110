import zipfile
import os
import sys
import shutil

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
    
    sys.stdout = f
    try:
      execfile(problem, {})
    finally:
      sys.stdout = orig


problem418 = os.path.join("assignments", "project1", "problem_4_18.py")
output418 = os.path.join("assignments", "project1", "problem_4_18_result.txt")
EvaluateProblem(problem418, output418)


problem421 = os.path.join("assignments", "project1", "problem_4_21.py")
output421 = os.path.join("assignments", "project1", "problem_4_21_result.txt")
EvaluateProblem(problem421, output421)

'''
Create a zip archive with all the .py files in meam2110/
Add in generated output files from textbook problems
'''
with zipfile.ZipFile(os.path.join(os.getcwd(), "assignments", "project1_submission.zip"), mode="w") as archive:
  archive.write(output418)
  archive.write(output421)
  for file in os.listdir('meam2110'):
    print(file)
    if file.endswith(".py"):
      archive.write(os.path.join("meam2110", file))
