from monthly_record import record

record = record("fgf", "gfk", 2022, 7)
record.write_to_file("gfk2207.txt")
record.load("fgf", "gfk", 2022, 8)
record.write_to_file("gfk2208.txt")
record.load("fgf", "gfk", 2022, 9)
record.write_to_file("gfk2209.txt")
##record.get_day(29)