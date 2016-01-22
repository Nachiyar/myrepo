from fit.ColumnFixture import ColumnFixture

class Division(ColumnFixture):
  _typeDict={
      "numerator": "Float",
      "denominator": "Float",
      "quotient": "Float",
      "quotient.charBounds": "99",
  }
  numerator = 0.0
  denominator = 0.0

  def quotient(self):
      return self.numerator / self.denominator
