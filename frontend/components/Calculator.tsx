'use client';

import React from 'react';
import { motion } from 'framer-motion';
import { useCalculator } from '@/store/calculator';
import Display from './Display';
import Button from './Button';
import styles from '@/styles/calculator.module.scss';

export const Calculator: React.FC = () => {
  const {
    handleNumber,
    handleDecimal,
    handleOperation,
    handleEquals,
    handleClear,
    handleDelete,
    toggleUpsideDown,
  } = useCalculator();

  // Sound effects
  const playBeep = React.useCallback(() => {
    try {
      const audioContext = new (window.AudioContext ||
        (window as any).webkitAudioContext)();
      const oscillator = audioContext.createOscillator();
      const gainNode = audioContext.createGain();

      oscillator.connect(gainNode);
      gainNode.connect(audioContext.destination);

      oscillator.frequency.value = 800;
      oscillator.type = 'sine';

      gainNode.gain.setValueAtTime(0.1, audioContext.currentTime);
      gainNode.gain.exponentialRampToValueAtTime(
        0.01,
        audioContext.currentTime + 0.1
      );

      oscillator.start(audioContext.currentTime);
      oscillator.stop(audioContext.currentTime + 0.1);
    } catch (e) {
      // AudioContext not available
    }
  }, []);

  const handleButtonClick = React.useCallback(
    (action: () => void) => {
      playBeep();
      action();
    },
    [playBeep]
  );

  const handleDisplayClick = () => {
    toggleUpsideDown();
  };

  return (
    <div className={styles.container}>
      <motion.div
        className={styles.wrapper}
        initial={{ scale: 0.8, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        transition={{ type: 'spring', stiffness: 100, damping: 15 }}
      >
        <div className={styles.calculator}>
          <div className={styles.title}>CALC-1980</div>
          <div onClick={handleDisplayClick} style={{ cursor: 'pointer' }}>
            <Display />
          </div>
          <div className={styles.buttonGrid}>
            {/* Row 1 */}
            <Button
              label="AC"
              onClick={() => handleButtonClick(handleClear)}
              type="clear"
              dataButton="clear"
            />
            <Button
              label="DEL"
              onClick={() => handleButtonClick(handleDelete)}
              type="clear"
              dataButton="delete"
            />
            <Button
              label="C"
              onClick={() => handleButtonClick(() => handleClear())}
              type="clear"
              dataButton="c"
            />
            <Button
              label="÷"
              onClick={() => handleButtonClick(() => handleOperation('divide'))}
              type="operation"
              dataButton="divide"
            />

            {/* Row 2 */}
            <Button
              label="7"
              onClick={() => handleButtonClick(() => handleNumber(7))}
              dataButton="7"
            />
            <Button
              label="8"
              onClick={() => handleButtonClick(() => handleNumber(8))}
              dataButton="8"
            />
            <Button
              label="9"
              onClick={() => handleButtonClick(() => handleNumber(9))}
              dataButton="9"
            />
            <Button
              label="×"
              onClick={() => handleButtonClick(() => handleOperation('multiply'))}
              type="operation"
              dataButton="multiply"
            />

            {/* Row 3 */}
            <Button
              label="4"
              onClick={() => handleButtonClick(() => handleNumber(4))}
              dataButton="4"
            />
            <Button
              label="5"
              onClick={() => handleButtonClick(() => handleNumber(5))}
              dataButton="5"
            />
            <Button
              label="6"
              onClick={() => handleButtonClick(() => handleNumber(6))}
              dataButton="6"
            />
            <Button
              label="−"
              onClick={() => handleButtonClick(() => handleOperation('subtract'))}
              type="operation"
              dataButton="subtract"
            />

            {/* Row 4 */}
            <Button
              label="1"
              onClick={() => handleButtonClick(() => handleNumber(1))}
              dataButton="1"
            />
            <Button
              label="2"
              onClick={() => handleButtonClick(() => handleNumber(2))}
              dataButton="2"
            />
            <Button
              label="3"
              onClick={() => handleButtonClick(() => handleNumber(3))}
              dataButton="3"
            />
            <Button
              label="+"
              onClick={() => handleButtonClick(() => handleOperation('add'))}
              type="operation"
              dataButton="add"
            />

            {/* Row 5 */}
            <Button
              label="0"
              onClick={() => handleButtonClick(() => handleNumber(0))}
              dataButton="0"
            />
            <Button
              label="."
              onClick={() => handleButtonClick(handleDecimal)}
              dataButton="decimal"
            />
            <Button
              label="="
              onClick={() => handleButtonClick(handleEquals)}
              type="equals"
              dataButton="equals"
            />
            <Button
              label="!!"
              onClick={() => handleButtonClick(toggleUpsideDown)}
              type="operation"
              dataButton="upsidedown"
            />
          </div>
        </div>
        <div className={styles.demogorgon}>
          <svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
            <circle cx="30" cy="30" r="8" fill="#FF0000" />
            <circle cx="70" cy="30" r="8" fill="#FF0000" />
            <circle cx="25" cy="35" r="3" fill="#000000" />
            <circle cx="75" cy="35" r="3" fill="#000000" />
            <path
              d="M 50 45 Q 35 60 30 75 Q 50 85 70 75 Q 65 60 50 45"
              fill="#FF0000"
              stroke="#FF6B9D"
              strokeWidth="1"
            />
            <path
              d="M 40 55 Q 50 65 60 55"
              stroke="#FF6B9D"
              strokeWidth="1"
              fill="none"
            />
          </svg>
        </div>
      </motion.div>
    </div>
  );
};

export default Calculator;
