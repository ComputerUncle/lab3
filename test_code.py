import lab2.code as code


def test_bmi_normal_weight():
 x = 0

 assert (code.calculate_bmi(1,20)==x)

def test_bmi_over_weight():
 x = -1

 assert (code.calculate_bmi(1,18)==x)

def test_bmi_under_weight():
 x = 1

 assert (code.calculate_bmi(1,26)==x)
