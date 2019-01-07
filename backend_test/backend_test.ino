#define METADATALEN 8
#define BUFLEN 120

void setup() {

  Serial.begin(115200);
  while (!Serial) {
    ; // wait for serial port to connect. 
    }
  
}

void loop() {

  //send 128 byte packet over UART
  
  static uint8_t ID = 1;
  
  uint32_t timestamp = 6787;

  uint8_t meta_data[METADATALEN];
  meta_data[0] = ID;
  meta_data[4] = (uint8_t)(timestamp & 0xFF);
  meta_data[5] = (uint8_t)((timestamp >> 8) & 0xFF);
  meta_data[6] = (uint8_t)((timestamp >> 16) & 0xFF);
  meta_data[7] = (uint8_t)((timestamp >> 24) & 0xFF);
  
  uint8_t buffer_data[BUFLEN];

  for(int i = 0; i < BUFLEN; i++){
    buffer_data[i] = i & 0xFF;
  }
  uint8_t start_byte = 0x7E;
  Serial.write(&start_byte, 1);
  Serial.write(meta_data, sizeof(meta_data));
  Serial.write(buffer_data, sizeof(buffer_data));

  if(ID==1) ID=2;
  else ID=1;

  delay(3000);
}
