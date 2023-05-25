
import appo_module_02 as am2

Weight = float(input('무게(Kg): '))
Height = float(input('키(m): '))

UBmi = am2.BmiAlgorithm(Weight, Height)
UBmi.calculatorBMI()
UBmi.printUserCondition()