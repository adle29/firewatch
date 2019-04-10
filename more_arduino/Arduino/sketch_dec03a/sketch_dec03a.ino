//LIBRARIES
//#include <LiquidCrystal.h>
//LiquidCrystal lcd(13, 12, 5, 4, 3, 2);

//VARIABLES
int RED_LED = 9;
int GREEN_LED = 10;

//METHODS
void setup() {
  Serial.begin(9600);
  Serial.print("starting program");
  pinMode(RED_LED,OUTPUT);
  pinMode(GREEN_LED,OUTPUT);
  
//  lcd.begin(16, 2);
//  lcd.println("FIREWATCH INIT");
 }

float getTemperatureReading(){
   int reading = analogRead(A1);  
   float voltage = reading * 5.0;
         voltage /= 1024.0; 
   float temperatureC = (voltage - 0.5) * 100 ;
   return temperatureC;
}

int getGasReading(){
  return analogRead(A0);
}

void setAlarm(int gasLevel){
  if (gasLevel > 100) {
    digitalWrite(RED_LED, HIGH);
  } else {
    digitalWrite(RED_LED, LOW);
  }
}


//MAIN 
void loop() {
//  lcd.clear();
  digitalWrite(GREEN_LED, HIGH);
  digitalWrite(RED_LED, LOW);

  //sensors
  int temp = getTemperatureReading();
  int gasLevel = getGasReading();
  String s1 = "Gas level: " + String(gasLevel);
  String s2 = "Temp: " + String(temp);

  //monitor
  setAlarm(gasLevel);

  //log 
  Serial.println(s1);
  Serial.println(s2);

  //print 
//  lcd.setCursor(0, 0); 
//  lcd.print(s1);
//  lcd.setCursor(0, 1); 
//  lcd.print(s2);
  
  delay(2000);
}






