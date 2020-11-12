import unittest
from unittest import mock
import calrand

class CalRandTest(unittest.TestCase):
    def check_add_assert(self, val_1, val_2, expected):
        result = calrand.add(val_1, val_2)
        self.assertEqual(expected, result)
    # add function
    def test_cal_add_100_200_get_300(self):
        val_1 = 100
        val_2 = 200
        expected = 300
        self.check_add_assert(val_1, val_2, expected)
    def test_cal_add_100_n200_get_n100(self):
        val_1 = 100
        val_2 = -200
        expected = -100
        self.check_add_assert(val_1, val_2, expected)
    def test_cal_add_n100_200_get_100(self):
        val_1 = -100
        val_2 = 200
        expected = 100
        self.check_add_assert(val_1, val_2, expected)
    def test_cal_add_n100_n200_get_n300(self):
        val_1 = -100
        val_2 = -200
        expected = -300
        self.check_add_assert(val_1, val_2, expected)
    # subtract function
    def test_cal_sub_100_200_get_n100(self):
        result = calrand.subtract(100, 200)
        expected = -100
        self.assertEqual(expected, result)
    def test_cal_sub_100_n200_get_300(self):
        result = calrand.subtract(100, -200)
        expected = 300
        self.assertEqual(expected, result)
    def test_cal_sub_n100_200_get_n300(self):
        result = calrand.subtract(-100, 200)
        expected = -300
        self.assertEqual(expected, result)           
    def test_cal_sub_n100_n200_get_100(self):
        result = calrand.subtract(-100, -200)
        expected = 100
        self.assertEqual(expected, result)
# multiply function
    def test_cal_mul_100_200_get_20000(self):
        result = calrand.multiply(100, 200)
        expected = 20000
        self.assertEqual(expected, result)
    def test_cal_mul_100_n200_get_n20000(self):
        result = calrand.multiply(100, -200)
        expected = -20000
        self.assertEqual(expected, result)
    def test_cal_mul_n100_200_get_n20000(self):
        result = calrand.multiply(-100, 200)
        expected = -20000
        self.assertEqual(expected, result)       
    def test_cal_mul_n100_n200_get_20000(self):
        result = calrand.multiply(-100, -200)
        expected = 20000
        self.assertEqual(expected, result)
    def test_cal_mul_0_200_get_0(self):
        result = calrand.multiply(0, 200)
        expected = 0
        self.assertEqual(expected, result)
    def test_cal_mul_0_0_get_0(self):
        result = calrand.multiply(0, 0)
        expected = 0
        self.assertEqual(expected, result)
    # divide function
    def test_cal_div_100_200_get_f0p5(self):
        result = calrand.divide(100, 200)
        expected = 0.5
        self.assertEqual(expected, result)
    def test_cal_div_100_n200_get_nf0p5(self):
        result = calrand.divide(100, -200)
        expected = -0.5
        self.assertEqual(expected, result)
    def test_cal_div_n100_200_get_nf0p5(self):
        result = calrand.divide(-100, 200)
        expected = -0.5
        self.assertEqual(expected, result)      
    def test_cal_div_n100_n200_get_f0p5(self):
        result = calrand.divide(-100, -200)
        expected = 0.5
        self.assertEqual(expected, result)
    def test_cal_div_0_200_get_0(self):
        result = calrand.divide(0, 200)
        expected = 0
        self.assertEqual(expected, result)
    def test_cal_div_0_0_get_error(self):
        result = calrand.divide(0, 0)
        expected = 'divide by zero exception'
        self.assertEqual(expected, result)
    # sin function 
    def test_cal_sin_0_get_0(self):
        result = calrand.sin(0)
        expected = 0
        self.assertEqual(expected, result)
    def test_cal_sin_1p5_get_0p997(self):
        result = calrand.sin(1.5)
        expected = 0.997
        self.assertEqual(expected, result)
    def test_cal_sin_n1p5_get_n0p997(self):
        result = calrand.sin(-1.5)
        expected = -0.997
        self.assertEqual(expected, result)
    # cosine function 
    def test_cal_cos_0_get_1(self):
        result = calrand.cosine(0)
        expected = 1
        self.assertEqual(expected, result)
    def test_cal_cos_1p5_get_0p07(self):
        result = calrand.cosine(1.5)
        expected = 0.071
        self.assertEqual(expected, result)
    def test_cal_cos_n1p5_get_0p07(self):
        result = calrand.cosine(-1.5)
        expected = 0.071
        self.assertEqual(expected, result)
    # tan function 
    def test_cal_tan_0_get_1(self):
        result = calrand.tan(0)
        expected = 0
        self.assertEqual(expected, result)
    def test_cal_tan_1p5_get_0p07(self):
        result = calrand.tan(1.5)
        expected = 14.101
        self.assertEqual(expected, result)
    def test_cal_tan_n1p5_get_0p07(self):
        result = calrand.tan(-1.5)
        expected = -14.101
        self.assertEqual(expected, result)
    # square root function 
    def test_cal_sqrt_0_get_0(self):
        result = calrand.sqrt(0)
        expected = 0
        self.assertEqual(expected, result)
    def test_cal_sqrt_1p5_get_1p225(self):
        result = calrand.sqrt(1.5)
        expected = 1.225
        self.assertEqual(expected, result)
    def test_cal_sqrt_n1p5_get_error(self):
        result = calrand.sqrt(-1.5)
        expected = 'sqrt of negative number'
        self.assertEqual(expected, result)
    # pow function
    def test_cal_pow_0_0_get_1(self):
        result = calrand.pow(0, 0)
        expected = 1
        self.assertEqual(expected, result)
    def test_cal_pow_5_2_get_25(self):
        result = calrand.pow(5, 2)
        expected = 25
        self.assertEqual(expected, result)
    def test_cal_pow_5_n2_get_0p04(self):
        result = calrand.pow(5, -2)
        expected = 0.04
        self.assertEqual(expected, result)
    def test_cal_pow_n5_2_get_25(self):
        result = calrand.pow(-5, 2)
        expected = 25
        self.assertEqual(expected, result)
    def test_cal_pow_n5_n2_get_0p04(self):
        result = calrand.pow(-5, -2)
        expected = 0.04
        self.assertEqual(expected, result)
    def test_cal_pow_0_n0p1_get_error(self):
        result = calrand.pow(0, -0.1)
        expected = 'math error'
        self.assertEqual(expected, result)
    def test_cal_pow_0_n5_get_error(self):
        result = calrand.pow(0, -5)
        expected = 'math error'
        self.assertEqual(expected, result)
    # bmi function
    def test_cal_bmi_80_1p8_get_24p691(self):
        result = calrand.bmi(80, 1.80)
        expected = 24.691
        self.assertEqual(expected, result) 
    def test_cal_bmi_n80_1p8_get_error(self):
        result = calrand.bmi(-80, 1.80)
        expected = 'weight or height less than 0'
        self.assertEqual(expected, result) 
    def test_cal_bmi_80_n1p8_get_error(self):
        result = calrand.bmi(80, -1.80)
        expected = 'weight or height less than 0'
        self.assertEqual(expected, result) 
    def test_cal_bmi_n80_n1p8_get_error(self):
        result = calrand.bmi(-80, -1.80)
        expected = 'weight or height less than 0'
        self.assertEqual(expected, result) 
    # random function
    @mock.patch('calrand.random.randint')
    def test_rand_random_num_10_20_get_15(self, randmock):
        expected = 15
        randmock.return_value = 15
        result = calrand.random_num(10, 20)
        self.assertEqual(expected, result) 
    #-------------------------------------------------------------------
    # check value 
    # 1 parameter
    def test_check_val_1_by_5_get_False(self):
        expected = False
        result = calrand.check_val_1(5)
        self.assertEqual(expected, result) 
    def test_check_val_1_by_ccc_get_True(self):
        expected = True
        result = calrand.check_val_1('ccc')
        self.assertEqual(expected, result) 
    # 2 parameters
    def test_check_val_2_by_5_10_get_False(self):
        expected = False
        result = calrand.check_val_2(5, 10)
        self.assertEqual(expected, result) 
    def test_check_val_2_by_5_ccc_get_True(self):
        expected = True
        result = calrand.check_val_2(5, 'ccc')
        self.assertEqual(expected, result) 
    def test_check_val_2_by_ccc_5_get_True(self):
        expected = True
        result = calrand.check_val_2('ccc', 5)
        self.assertEqual(expected, result) 
    def test_check_val_2_by_aaa_ccc_get_True(self):
        expected = True
        result = calrand.check_val_2('aaa', 'ccc')
        self.assertEqual(expected, result) 
    #-------------------------------------------------------------------
    # check input value function
    # 1 input
    @mock.patch('builtins.input', lambda *args: 5)
    @mock.patch('calrand.check_val_1')
    def test_input_val_give_option_5_get_1_value(self, mock_1):
        expected = 5    #return value
        mock_1.return_value = False
        result = calrand.input_val(5)
        self.assertEqual(expected, result) 
    # 2 inputs
    @mock.patch('builtins.input', lambda *args: 5)
    @mock.patch('calrand.check_val_1')
    def test_input_val_give_option_1_get_2_value(self, mock_1):
        expected = 5, 5    #return value
        mock_1.return_value = False
        result = calrand.input_val(1)
        self.assertEqual(expected, result) 
    #------------------------------------------------------------------
    # test options function
    # option 1
    @mock.patch('calrand.input_val')
    def test_options_1_by_give_1_2_get_3(self, mock):
        expected = 3
        mock.return_value = 1, 2
        result = calrand.options(1)
        self.assertEqual(expected, result)     
    # option 2
    @mock.patch('calrand.input_val')
    def test_options_2_by_give_20_10_get_10(self, mock):
        expected = 10
        mock.return_value = 20, 10
        result = calrand.options(2)
        self.assertEqual(expected, result)  
    # option 3
    @mock.patch('calrand.input_val')
    def test_options_3_by_give_1_2_get_2(self, mock):
        expected = 2
        mock.return_value = 1, 2
        result = calrand.options(3)
        self.assertEqual(expected, result) 
    # option 4
    @mock.patch('calrand.input_val')
    def test_options_4_by_give_1_2_get_0p5(self, mock):
        expected = 0.5
        mock.return_value = 1, 2
        result = calrand.options(4)
        self.assertEqual(expected, result)   
    # option 5
    @mock.patch('calrand.input_val')
    def test_options_5_by_give_1_get_0p841(self, mock):
        expected = 0.841
        mock.return_value = 1
        result = calrand.options(5)
        self.assertEqual(expected, result)  
    # option 6
    @mock.patch('calrand.input_val')
    def test_options_6_by_give_1_get_0p540(self, mock):
        expected = 0.540
        mock.return_value = 1
        result = calrand.options(6)
        self.assertEqual(expected, result)  
    # option 7
    @mock.patch('calrand.input_val')
    def test_options_7_by_give_1_get_1p557(self, mock):
        expected = 1.557
        mock.return_value = 1
        result = calrand.options(7)
        self.assertEqual(expected, result)  
    # option 8
    @mock.patch('calrand.input_val')
    def test_options_by_8_and_give_9_get_3(self, mock):
        expected = 3
        mock.return_value = 9
        result = calrand.options(8)
        self.assertEqual(expected, result) 
    # option 9
    @mock.patch('calrand.input_val')
    def test_options_9_by_give_5_2_get_25(self, mock):
        expected = 25
        mock.return_value = 5, 2
        result = calrand.options(9)
        self.assertEqual(expected, result)  
    # option 10
    @mock.patch('calrand.input_val')
    def test_options_10_by_give_80_1p8_get_24p691(self, mock):
        expected = 24.691
        mock.return_value = 80, 1.80
        result = calrand.options(10)
        self.assertEqual(expected, result)  
    # option 11
    @mock.patch('calrand.input_val')
    @mock.patch('calrand.random_num')
    def test_options_11_by_give_5_10_get_7(self, mock_1, mock_2):
        expected = 7
        mock_2.return_value = 5, 10
        mock_1.return_value = 7
        result = calrand.options(11)
        self.assertEqual(expected, result)  
    #------------------------------------------------------------