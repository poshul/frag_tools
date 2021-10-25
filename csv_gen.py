# Author Samuel Wein
# Produces a CSV of hits from an idXML file
import pyopenms
from re import sub
import sys

def main() -> int:
  args = sys.argv[1:]
  if len(args) != 2:
      print("usage: python csv_gen.py $inputfile $outputfile")
      exit()
  doParse(args[0],args[1])
  return 0

def doParse(input_file, output_file):
  f = open(output_file,'w')
  protein_ids = []
  peptide_ids = []
  pyopenms.IdXMLFile().load(input_file,protein_ids, peptide_ids)
  for i in peptide_ids:
      for j in i.getHits():
          seqstring = j.getMetaValue("label")
          f.write(seqstring + '\n')
          f.write("Fragment,ChargeState,m/z,intensity\n")
          for k in j.getPeakAnnotations():
              f.write(k.annotation + ',' + str(k.charge) + ',' + str(k.mz) + ',' + str(k.intensity) + '\n')
          f.write('\n')
  f.close()

if __name__ == '__main__':
  sys.exit(main())

