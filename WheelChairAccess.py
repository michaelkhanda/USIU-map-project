from kanren import *

BuildingsAccess = Relation()
OutsideAccess = Relation()
InsideAccess = Relation()

facts(BuildingsAccess, ("admin_block", "Access"),
      ("lillian_beam", "Access"),
      ("village", "No Access"),
      ("cafeteria", "Access"),
      ("auditorium", "Access"),
      ("csob", "Access"),
      ("library", "Access"),
      ("students_centre", "Access"),
      ("science_complex", "Access"),
      ("shss", "Access"))

facts(OutsideAccess, ("admin_block", "Via Ramp"),
      ("lillian_beam", "Via Ramp"),
      ("village", "No Access"),
      ("cafeteria", "Via Ramp"),
      ("auditorium", "Via Ramp"),
      ("csob", "Flat ground"),
      ("library", "Via Ramp"),
      ("students_centre", "Flat ground"),
      ("science_complex", "Flat ground"),
      ("shss", "Via Ramp"))

facts(InsideAccess, ("admin_block", "No Access"),
      ("lillian_beam", "No Access"),
      ("village", "No Access"),
      ("cafeteria", "No Access"),
      ("auditorium", "No Access"),
      ("csob", "Via elevator"),
      ("library", "Via elevator"),
      ("students_centre", "Via elevator"),
      ("science_complex", "Via elevator"),
      ("shss", "Via elevator"))

BuildingsAccess_V, OutsideAccess_V, InsideAccess_V, Access_V = var(), var(), var(), var()
print("All USIU buildings with Wheelchair accesses",
      (run(0, Access_V, BuildingsAccess(Access_V, BuildingsAccess_V), BuildingsAccess(Access_V, "Access"))))
print("All USIU buildings with no Wheelchair accesses",
      (run(0, Access_V, BuildingsAccess(Access_V, BuildingsAccess_V), BuildingsAccess(Access_V, "No Access"))))
print("Buildings with outside wheelchair accesses in USIU using a ramp:",
      (run(0, Access_V, OutsideAccess(Access_V, BuildingsAccess_V), OutsideAccess(Access_V, "Via Ramp"))))
print("Buildings with outside wheelchair accesses in USIU using flat ground:",
      (run(0, Access_V, OutsideAccess(Access_V, BuildingsAccess_V),
           OutsideAccess(Access_V, "Flat ground"))))
print("Buildings with no outside wheelchair accesses in USIU:",
      (run(0, Access_V, OutsideAccess(Access_V, BuildingsAccess_V),
           OutsideAccess(Access_V, "No Access"))))
print("Buildings with inside accesses of wheelchairs in USIU using elevators:",
      (run(0, Access_V, InsideAccess(Access_V, BuildingsAccess_V),
           InsideAccess(Access_V, "Via elevator"))))
print("Buildings with no inside accesses of wheelchairs in USIU:",
      (run(0, Access_V, InsideAccess(Access_V, BuildingsAccess_V),
           InsideAccess(Access_V, "No Access"))))

