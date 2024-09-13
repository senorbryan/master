// Constants are variables that cannot be changed
// Float values can hold values with decimal points such as 2.5

const int sensorPin = 40;
const float baselineTemp = 20.0;

void setup()
{
  // Serial.begin() connects the Arduino to the computer, allowing us to see values from the analog input on the computer
  Serial.begin(9600);
  
  // The for loop will run through pins 2-4 on the Arduino, much faster than assigning names to each LED
  for (int pinNumber = 2; pinNumber < 5; pinNumber++)
  {
    pinMode(pinNumber, OUTPUT);
    digitalWrite(pinNumber, LOW);
  }
}

// loop() will use local variable sensorVal to store a reading from the temperature sensor
void loop()
{
  // analogRead summons the argument value from the sensor
  int sensorVal = analogRead(sensorPin);

  // Serial.print() sends information from the Arduino to a connected computer
  Serial.print(sensorVal);

  // The equation to find out the voltage is: (value from temperature sensor / 1024.0) * 5.0
  float voltage = (sensorVal / 1024.0) * 5.0;
  Serial.print(voltage);

  // 10 milivolts of charge is equivalent to a temperature change of 1 degree Celcius
  // The sensor can also pick up values below 0 degrees
  // This equation will offset for values below freezing point (0 degrees) by subtracting 0.5 from the voltage, multiplying it by 100, and storing it in a temperature variable
  Serial.print(", Volts ");
  Serial.print(voltage);
  Serial.print(", degrees C: ");

  // Voltage to temperature equation
  float temperature = (voltage - 0.5) * 100;
  Serial.println(temperature); //Serial.println will print the string to a different line in the terminal

  // A conditional statement where no LEDs will light up if temperature is less than 2 degrees above the baseline 
  if (temperature = baselineTemp + 2)
  {
    digitalWrite(2, LOW);
    digitalWrite(3, LOW);
    digitalWrite(3, LOW);
  }

  // A conditional statement where one LED will light up if the temperature is 2 degrees greater than the baseline and less than 4 degrees above the baseline
  // && operator means 'and'
  else if (temperature >= baselineTemp + 2 && temperature < baselineTemp + 4)
  {
    digitalWrite(2, HIGH);
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
  }

  // A conditional statement where two LEDs will light up if the temperature is 4 degrees greater than the baseline and less than 6 degrees above the baseline
  else if (temperature >= baselineTemp + 4 && temperature < baselineTemp + 6)
  {
    digitalWrite(2, HIGH);
    digitalWrite(3, HIGH);
    digitalWrite(4, LOW);
  }

  // A conditional statement where all 3 LEDs will light up if the temperature is 6 degrees or greater above the baseline
  else if (temperature >= baselineTemp + 6)
  {
    digitalWrite(2, HIGH);
    digitalWrite(3, HIGH);
    digitalWrite(4, HIGH);
  }

  delay(3);

}