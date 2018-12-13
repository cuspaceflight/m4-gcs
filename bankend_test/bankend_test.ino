void setup() {

  Serial.begin(57600);
  while (!Serial) {
    ; // wait for serial port to connect. 
    }
  
}

void loop() {

  //send 128 byte packet over UART
  
  uint8_t ID = 0b01000101;
  uint32_t timestamp = 6787;

  uint8_t meta_data[8];
  meta_data[0] = ID;
  meta_data[4] = (uint8_t)(timestamp & 0xFF);
  meta_data[5] = (uint8_t)((timestamp >> 8) & 0xFF);
  meta_data[6] = (uint8_t)((timestamp >> 16) & 0xFF);
  meta_data[7] = (uint8_t)((timestamp >> 24) & 0xFF);
  
  uint64_t Data = 450648;
  uint8_t buffer_data[8];

  for(int i = 0; i <8; i++){
    buffer_data[i] = (uint8_t)(Data >> i) & 0xFF;
  }
  
  
  Serial.write(meta_data, 4);
  Serial.write(buffer_data, 4);
}
