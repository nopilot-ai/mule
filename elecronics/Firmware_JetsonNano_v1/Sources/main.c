/**
  ******************************************************************************
  * @file    IWDG/IWDG_Reset/main.c 
  * @author  MCD Application Team
  * @version V3.5.0
  * @date    08-April-2011
  * @brief   Main program body.
  ******************************************************************************
  * @attention
  *
  * THE PRESENT FIRMWARE WHICH IS FOR GUIDANCE ONLY AIMS AT PROVIDING CUSTOMERS
  * WITH CODING INFORMATION REGARDING THEIR PRODUCTS IN ORDER FOR THEM TO SAVE
  * TIME. AS A RESULT, STMICROELECTRONICS SHALL NOT BE HELD LIABLE FOR ANY
  * DIRECT, INDIRECT OR CONSEQUENTIAL DAMAGES WITH RESPECT TO ANY CLAIMS ARISING
  * FROM THE CONTENT OF SUCH FIRMWARE AND/OR THE USE MADE BY CUSTOMERS OF THE
  * CODING INFORMATION CONTAINED HEREIN IN CONNECTION WITH THEIR PRODUCTS.
  *
  * <h2><center>&copy; COPYRIGHT 2011 STMicroelectronics</center></h2>
  ******************************************************************************
  */

/* Includes ------------------------------------------------------------------*/
#include "stm32f10x.h"
#include "inits.h"
#include "modbus.h"
#include "mb_regs.h"
#include "main.h"

uint16_t adc_end[5];
uint32_t adc_flag = 0;
uint16_t adc_data[ADC_ARR_LENGT*2][ADC_CH_CNT];

int main(void)
{
  //RCC->CFGR |= RCC_MCO_PLLCLK_Div2;
  init_sysclk();
  IWDG_WriteAccessCmd(IWDG_WriteAccess_Enable);
  init_gpio();
  init_adc(); 
  init_modbus(115200);
  init_ppm();
  mb.u8id = 1;
  
  /*GPIO_InitTypeDef GPIO_InitStructure;
  GPIO_InitStructure.GPIO_Pin = GPIO_Pin_8;
  GPIO_InitStructure.GPIO_Speed = GPIO_Speed_50MHz;
  GPIO_InitStructure.GPIO_Mode = GPIO_Mode_AF_PP;
  GPIO_Init(GPIOA, &GPIO_InitStructure);*/
  while (1)
  {
    IWDG_ReloadCounter(); 
    if(mb.flag & 0x01)
    {
      mb.flag &=~ 1;
      mb_poll();
      USART_ITConfig(USART1, USART_IT_RXNE, ENABLE);
      mb.u16InCnt = 0;
      
      GPIO_WriteBit(GPIOB, GPIO_Pin_5, !mb.registers.one[mbREG_PPM_PON]);
      TIM_SetCompare1(TIM4, mb.registers.one[mbREG_PPM_4]);
      TIM_SetCompare2(TIM4, mb.registers.one[mbREG_PPM_3]);
      TIM_SetCompare3(TIM4, mb.registers.one[mbREG_PPM_2]);
      TIM_SetCompare4(TIM4, mb.registers.one[mbREG_PPM_1]);
      
      mb.registers.one[mbREG_adc_Vbat] = (uint16_t)adc_end[0];
      mb.registers.one[mbREG_adc_Ibat] = (uint16_t)adc_end[1];
      mb.registers.one[mbREG_adc_Vjet] = (uint16_t)adc_end[3];
      mb.registers.one[mbREG_adc_Ijet] = (uint16_t)adc_end[2];
      mb.registers.one[mbREG_adc_5V] = (uint16_t)adc_end[4];
      //led_toggle();
    }   
    if (adc_flag & 2)
    {
      adc_flag &=~ 2;
      uint16_t part = 0;
      if (adc_flag & 1)
        part = ADC_ARR_LENGT;
      uint32_t adc_middle[ADC_CH_CNT];
      for (uint16_t cnt_ch = 0; cnt_ch < ADC_CH_CNT; cnt_ch++)
      {
        adc_middle[cnt_ch] = 0;
        for (uint16_t cnt = 0; cnt < ADC_ARR_LENGT; cnt++)
        {
          adc_middle[cnt_ch] += adc_data[cnt + part][cnt_ch];
        }
        adc_end[cnt_ch] = adc_middle[cnt_ch] / ADC_ARR_LENGT;
      }
    } 
  }
}

void led_toggle(void)
{
  if (GPIOC->ODR & GPIO_ODR_ODR13)
    GPIOC->BSRR |= GPIO_BSRR_BR13; 
  else
    GPIOC->BSRR |= GPIO_BSRR_BS13;  
}


#ifdef  USE_FULL_ASSERT

/**
  * @brief  Reports the name of the source file and the source line number
  *         where the assert_param error has occurred.
  * @param  file: pointer to the source file name
  * @param  line: assert_param error line source number
  * @retval None
  */
void assert_failed(uint8_t* file, uint32_t line)
{
  /* User can add his own implementation to report the file name and line number,
     ex: printf("Wrong parameters value: file %s on line %d\r\n", file, line) */

  /* Infinite loop */
  while (1)
  {}
}

#endif

/******************* (C) COPYRIGHT 2011 STMicroelectronics *****END OF FILE****/
