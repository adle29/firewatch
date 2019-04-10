#define LED 11
 
void setup() {
  Serial.begin(115200);
  Serial.println("MiCS-5524 demo!");
 
  pinMode(8, OUTPUT);
  pinMode(7, OUTPUT);
}
 
void loop() {
  digitalWrite(7, HIGH); 
  int reading = analogRead(A0);
  Serial.println(reading);

  if (reading > 400){
    digitalWrite(8, HIGH);
  } else {
    digitalWrite(8, LOW);
  }
  delay(10);
}
  
