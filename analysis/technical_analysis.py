#!/usr/bin/env python3
"""Technical analysis for Fincept Terminal"""

import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)

class TechnicalAnalysis:
    """Class for technical analysis indicators"""
    
    def __init__(self):
        pass
    
    def calculate_moving_average(self, data, period=20):
        """Calculate moving average"""
        try:
            if 'Close' not in data.columns:
                logger.error("Close column not found in data")
                return None
            
            ma = data['Close'].rolling(window=period).mean()
            return ma
        except Exception as e:
            logger.error(f"Error calculating moving average: {e}")
            return None
    
    def calculate_macd(self, data, fast_period=12, slow_period=26, signal_period=9):
        """Calculate MACD"""
        try:
            if 'Close' not in data.columns:
                logger.error("Close column not found in data")
                return None
            
            # Calculate EMA
            ema_fast = data['Close'].ewm(span=fast_period, adjust=False).mean()
            ema_slow = data['Close'].ewm(span=slow_period, adjust=False).mean()
            
            # Calculate MACD line
            macd_line = ema_fast - ema_slow
            
            # Calculate signal line
            signal_line = macd_line.ewm(span=signal_period, adjust=False).mean()
            
            # Calculate histogram
            histogram = macd_line - signal_line
            
            return {
                'macd_line': macd_line,
                'signal_line': signal_line,
                'histogram': histogram
            }
        except Exception as e:
            logger.error(f"Error calculating MACD: {e}")
            return None
    
    def calculate_rsi(self, data, period=14):
        """Calculate RSI"""
        try:
            if 'Close' not in data.columns:
                logger.error("Close column not found in data")
                return None
            
            # Calculate price changes
            delta = data['Close'].diff()
            
            # Separate gains and losses
            gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
            loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
            
            # Calculate RS and RSI
            rs = gain / loss
            rsi = 100 - (100 / (1 + rs))
            
            return rsi
        except Exception as e:
            logger.error(f"Error calculating RSI: {e}")
            return None
    
    def calculate_bollinger_bands(self, data, period=20, std_dev=2):
        """Calculate Bollinger Bands"""
        try:
            if 'Close' not in data.columns:
                logger.error("Close column not found in data")
                return None
            
            # Calculate moving average
            ma = data['Close'].rolling(window=period).mean()
            
            # Calculate standard deviation
            std = data['Close'].rolling(window=period).std()
            
            # Calculate upper and lower bands
            upper_band = ma + (std * std_dev)
            lower_band = ma - (std * std_dev)
            
            return {
                'ma': ma,
                'upper_band': upper_band,
                'lower_band': lower_band
            }
        except Exception as e:
            logger.error(f"Error calculating Bollinger Bands: {e}")
            return None
    
    def calculate_stochastic(self, data, k_period=14, d_period=3):
        """Calculate Stochastic Oscillator"""
        try:
            if 'High' not in data.columns or 'Low' not in data.columns or 'Close' not in data.columns:
                logger.error("Missing required columns for stochastic calculation")
                return None
            
            # Calculate highest high and lowest low
            highest_high = data['High'].rolling(window=k_period).max()
            lowest_low = data['Low'].rolling(window=k_period).min()
            
            # Calculate %K
            k = ((data['Close'] - lowest_low) / (highest_high - lowest_low)) * 100
            
            # Calculate %D
            d = k.rolling(window=d_period).mean()
            
            return {
                'k': k,
                'd': d
            }
        except Exception as e:
            logger.error(f"Error calculating Stochastic Oscillator: {e}")
            return None
