
#define ADC_CH_CNT 5
#define ADC_ARR_LENGT 199

#define DELAY_LEN 48
#define LED_COUNT 12
#define ARRAY_LEN DELAY_LEN + LED_COUNT*24

extern uint32_t adc_flag;
extern uint16_t adc_data[ADC_ARR_LENGT*2][ADC_CH_CNT];
void led_toggle(void);
void init_ws2812(void);

extern uint16_t led_ws2812[ARRAY_LEN];

struct adc_math
{
  uint16_t ch[ADC_CH_CNT];
  float V_bat;
  float I_bat;
  float V_jet;
  float I_jet;
  float V_5v;
  float Wh_bat;
  float Wh_jet;
  float W_bat;
  float W_jet;
};