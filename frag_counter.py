# Author Samuel Wein
# Sums the intensity of fragment types from an idXML file containg RNA identifications
import pyopenms
from re import sub
import sys

def main() -> int:
  args = sys.argv[1:]
  if len(args) != 2:
      print("usage: python frag_counter.py $inputfile $outputfile")
      exit()
  doParse(args[0],args[1])
  return 0

def doParse(input_file, output_file):
  f = open(output_file,'w')
  protein_ids = []
  peptide_ids = []
  f.write("sequence\tscore\ta\ta-B\tb\tc\td\tw\tx\ty\tz\n")
  pyopenms.IdXMLFile().load(input_file,protein_ids, peptide_ids)
  for i in peptide_ids:
      hits = i.getHits()
      for j in hits:
          annotations = j.getPeakAnnotations()
          ann_dict = {'a':0.0, 'a-B':0.0, 'b':0.0, 'c':0.0, 'd':0.0, 'w':0.0, 'x':0.0, 'y':0.0, 'z':0.0}
          for k in annotations:
              ion_type = sub(r'[0-9]+', '', k.annotation)
              ann_dict[ion_type] += k.intensity
          f.write(j.getMetaValue("label") + "\t" + str(j.getScore()) + "\t" + str(ann_dict["a"]) + "\t" + str(ann_dict["a-B"]) + "\t" + str(ann_dict["b"]) + "\t" + str(ann_dict["c"]) + "\t" + str(ann_dict["d"]) + "\t" + str(ann_dict["w"]) + "\t" + str(ann_dict["x"]) + "\t" + str(ann_dict["y"]) + "\t" + str(ann_dict["z"]) + "\n" )
  f.close()

if __name__ == '__main__':
  sys.exit(main())

