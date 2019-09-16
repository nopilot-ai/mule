
#define ADC_CH_CNT 5
#define ADC_ARR_LENGT 10

extern uint32_t adc_flag;
extern uint16_t adc_data[ADC_ARR_LENGT*2][ADC_CH_CNT];
void led_toggle(void);