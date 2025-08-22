def more():
    return "more"

more()



def test_abs_for_a_negative_number():
 
  # Arrange
  negative = -2
   
  # Act
  answer = abs(negative)
   
  # Assert
  assert answer == 2