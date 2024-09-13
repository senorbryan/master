int switchState = 0;

void setup()
{
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
}

void loop()
{
  switchState = digitalRead(2);
  
  // Condition for button not being pressed
  if (switchState == LOW)
  {
    digitalWrite(3, HIGH); // Green LED 
    digitalWrite(4, LOW); // Red LED 
    digitalWrite(5, LOW); // Red LED 
  }
  //Condition for button being pressed
  else 
  {
    digitalWrite(3, LOW); // Green LED
    digitalWrite(4, LOW);//Red LED 
    digitalWrite(5, HIGH); //Red LED

    delay(250); // Delay time of a quarter second
    
    // LED Toggle
    digitalWrite(4, HIGH);
    digitalWrite(5, LOW);
    delay(250); // Delay time of a quarter second

  }
}