import os;
import sys
sys.path.append('../../common')
from env_indigo import *

indigo = Indigo()
# load targets
targets = list(indigo.iterateSDFile("molecules/arom_targets.sdf"))
#targets = [ indigo.loadMoleculeFromFile("test.mol") ]
for t in targets:
   t.aromatize()
# load queries
queries = [indigo.loadQueryMolecule(x.rawData()) for x in indigo.iterateSDFile("molecules/arom_queries.sdf")]
#queries = [ indigo.loadQueryMoleculeFromFile("query.mol") ]
#indigo.dbgBreakpoint()
for i in range(len(queries)):
   queries[i].aromatize()
   queries[i].setName("#%s" % i)
query_results = {}
for q in queries:
   query_results[q.name()] = 0
for t in targets:
   #t.saveMolfile("aaa.mol")
   matcher = indigo.substructureMatcher(t)
   for q in queries:
      m = None
      #indigo.dbgBreakpoint()
      try:
         m = matcher.match(q)
      except IndigoException, e:
         sys.stderr.write("%s %s: %s\n" % (t.name(), q.name(), getIndigoExceptionText(e)))
      if m != None:
         query_results[q.name()] += 1
         cnt = matcher.countMatches(q)
         print("%s %s: %d" % (t.name(), q.name(), cnt))
print("\nResults per query:")
for q in queries:
   print("%s: %d" % (q.name(), query_results[q.name()]))
