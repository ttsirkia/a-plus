from django.test import TestCase

from .grade import calculate_grade


class GradeTest(TestCase):

    NORMAL_BOUNDS = [ 10, 20, 30, 40, 50 ]
    DIFFICULTY_BOUNDS = [
        [['A',1800],['B',0],['C',0]],
        [['A',1900],['B',400],['C',0]],
        [['A',1900],['B',875],['C',0]],
        [['A',1900],['B',875],['C',350]],
        [['A',1900],['B',875],['C',600]],
    ]
    GRADE_0 = { 'points':8, 'points_by_difficulty':{'A':1500,'B':200} }
    GRADE_1 = { 'points':10, 'points_by_difficulty':{'A':1800} }
    GRADE_2 = { 'points':25, 'points_by_difficulty':{'A':1900,'B':500}}
    GRADE_3 = { 'points':39, 'points_by_difficulty':{'A':1900,'B':875,'C':349}}
    GRADE_4 = { 'points':48, 'points_by_difficulty':{'A':1800,'B':775,'C':550}}
    GRADE_5 = { 'points':100, 'points_by_difficulty':{'A':1700,'B':0,'C':1775}}

    def test_normal_points(self):
        self.assertEquals(calculate_grade(self.GRADE_0, self.NORMAL_BOUNDS, False), 0)
        self.assertEquals(calculate_grade(self.GRADE_1, self.NORMAL_BOUNDS, False), 1)
        self.assertEquals(calculate_grade(self.GRADE_2, self.NORMAL_BOUNDS, False), 2)
        self.assertEquals(calculate_grade(self.GRADE_3, self.NORMAL_BOUNDS, True), 3)
        self.assertEquals(calculate_grade(self.GRADE_4, self.NORMAL_BOUNDS, False), 4)
        self.assertEquals(calculate_grade(self.GRADE_5, self.NORMAL_BOUNDS, False), 5)

    def test_difficulty_points(self):
        self.assertEquals(calculate_grade(self.GRADE_0, self.DIFFICULTY_BOUNDS, False), 0)
        self.assertEquals(calculate_grade(self.GRADE_1, self.DIFFICULTY_BOUNDS, False), 1)
        self.assertEquals(calculate_grade(self.GRADE_2, self.DIFFICULTY_BOUNDS, False), 2)
        self.assertEquals(calculate_grade(self.GRADE_3, self.DIFFICULTY_BOUNDS, False), 3)
        self.assertEquals(calculate_grade(self.GRADE_4, self.DIFFICULTY_BOUNDS, False), 1)
        self.assertEquals(calculate_grade(self.GRADE_5, self.DIFFICULTY_BOUNDS, False), 0)

    def test_padded_difficulty_points(self):
        self.assertEquals(calculate_grade(self.GRADE_0, self.DIFFICULTY_BOUNDS, True), 0)
        self.assertEquals(calculate_grade(self.GRADE_1, self.DIFFICULTY_BOUNDS, True), 1)
        self.assertEquals(calculate_grade(self.GRADE_2, self.DIFFICULTY_BOUNDS, True), 2)
        self.assertEquals(calculate_grade(self.GRADE_3, self.DIFFICULTY_BOUNDS, True), 3)
        self.assertEquals(calculate_grade(self.GRADE_4, self.DIFFICULTY_BOUNDS, True), 4)
        self.assertEquals(calculate_grade(self.GRADE_5, self.DIFFICULTY_BOUNDS, True), 5)
