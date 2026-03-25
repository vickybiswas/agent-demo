'use client';

import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import pacmanTheme from '../config/pacman-theme.json';
import styles from './Calculator.module.scss';
import '../styles/_pacman-theme.scss';

interface Ghost {
  name: string;
  color: string;
  personality: string;
}

export default function Calculator() {
  const [display, setDisplay] = useState('0');
  const [previousValue, setPreviousValue] = useState<number | null>(null);
  const [operation, setOperation] = useState<string | null>(null);
  const [newNumber, setNewNumber] = useState(true);
  const [scientificMode, setScientificMode] = useState(false);
  const [level, setLevel] = useState(1);
  const [pellets, setPellets] = useState<number[]>([]);

  const ghosts = pacmanTheme.theme.ghosts as Ghost[];
  const colors = pacmanTheme.theme.colors;

  // Sound effects using Web Audio API
  const playSound = (type: 'click' | 'result' | 'scientific' | 'power-up') => {
    const audioContext = new (window.AudioContext || (window as any).webkitAudioContext)();
    const oscillator = audioContext.createOscillator();
    const gainNode = audioContext.createGain();

    oscillator.connect(gainNode);
    gainNode.connect(audioContext.destination);

    const now = audioContext.currentTime;
    gainNode.gain.setValueAtTime(0.3, now);
    gainNode.gain.exponentialRampToValueAtTime(0.01, now + 0.2);

    switch (type) {
      case 'click':
        oscillator.frequency.value = 800;
        oscillator.start(now);
        oscillator.stop(now + 0.1);
        break;
      case 'scientific':
        oscillator.frequency.value = 1500;
        oscillator.start(now);
        oscillator.stop(now + 0.15);
        break;
      case 'power-up':
        oscillator.frequency.setValueAtTime(800, now);
        oscillator.frequency.exponentialRampToValueAtTime(1200, now + 0.3);
        oscillator.start(now);
        oscillator.stop(now + 0.3);
        break;
      case 'result':
        oscillator.frequency.value = 1200;
        oscillator.start(now);
        oscillator.stop(now + 0.2);
        break;
    }
  };

  // Handle number input
  const handleNumber = (num: string) => {
    playSound('click');
    if (newNumber) {
      setDisplay(num);
      setNewNumber(false);
    } else {
      setDisplay(display === '0' ? num : display + num);
    }
    addPellet();
  };

  // Handle decimal point
  const handleDecimal = () => {
    playSound('click');
    if (!display.includes('.')) {
      setDisplay(display + '.');
      setNewNumber(false);
    }
  };

  // Handle basic operations
  const handleOperation = (op: string) => {
    playSound('click');
    const inputValue = parseFloat(display);

    if (previousValue === null) {
      setPreviousValue(inputValue);
    } else if (operation) {
      const result = performOperation(previousValue, inputValue, operation);
      setDisplay(String(result));
      setPreviousValue(result);
    }

    setOperation(op);
    setNewNumber(true);
  };

  // Handle scientific operations
  const handleScientific = (op: string) => {
    playSound('scientific');
    const inputValue = parseFloat(display);
    let result = 0;

    switch (op) {
      case 'sqrt':
        result = inputValue >= 0 ? Math.sqrt(inputValue) : 0;
        break;
      case 'pow':
        result = Math.pow(inputValue, 2);
        break;
      case 'sin':
        result = Math.sin((inputValue * Math.PI) / 180);
        break;
      case 'cos':
        result = Math.cos((inputValue * Math.PI) / 180);
        break;
      case 'tan':
        result = Math.tan((inputValue * Math.PI) / 180);
        break;
      case 'log':
        result = inputValue > 0 ? Math.log10(inputValue) : 0;
        break;
      case 'ln':
        result = inputValue > 0 ? Math.log(inputValue) : 0;
        break;
      case 'factorial':
        result = calculateFactorial(inputValue);
        break;
      case 'reciprocal':
        result = inputValue !== 0 ? 1 / inputValue : 0;
        break;
      case 'percent':
        result = inputValue / 100;
        break;
      case 'pi':
        result = Math.PI;
        break;
      case 'e':
        result = Math.E;
        break;
    }

    setDisplay(String(Math.round(result * 1000000) / 1000000));
    setNewNumber(true);
    addPellet();
    playSound('power-up');
    setLevel(Math.min(level + 1, 9));
  };

  // Perform basic operations
  const performOperation = (prev: number, current: number, op: string): number => {
    switch (op) {
      case '+':
        return prev + current;
      case '-':
        return prev - current;
      case '*':
        return prev * current;
      case '/':
        return current !== 0 ? prev / current : 0;
      default:
        return current;
    }
  };

  // Calculate factorial
  const calculateFactorial = (n: number): number => {
    if (n < 0 || !Number.isInteger(n)) return 0;
    if (n === 0 || n === 1) return 1;
    let result = 1;
    for (let i = 2; i <= n; i++) {
      result *= i;
    }
    return result;
  };

  // Handle equals
  const handleEquals = () => {
    playSound('result');
    if (operation && previousValue !== null) {
      const result = performOperation(previousValue, parseFloat(display), operation);
      setDisplay(String(Math.round(result * 1000000) / 1000000));
      setPreviousValue(null);
      setOperation(null);
      setNewNumber(true);
      addPellet();
    }
  };

  // Handle clear
  const handleClear = () => {
    playSound('click');
    setDisplay('0');
    setPreviousValue(null);
    setOperation(null);
    setNewNumber(true);
    setPellets([]);
    setLevel(1);
  };

  // Add pellet animation
  const addPellet = () => {
    const pelletId = Date.now();
    setPellets((prev) => [...prev, pelletId]);
    setTimeout(() => {
      setPellets((prev) => prev.filter((id) => id !== pelletId));
    }, 1000);
  };

  // Toggle scientific mode
  const toggleScientific = () => {
    playSound('power-up');
    setScientificMode(!scientificMode);
  };

  return (
    <motion.div
      className="pacman-calculator"
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.5 }}
    >
      {/* Ghost sprites */}
      {ghosts.map((ghost, index) => (
        <motion.div
          key={ghost.name}
          className={`ghost ${ghost.name.toLowerCase()}`}
          style={{ background: ghost.color }}
          animate={{
            top: ['20px', '40px', '20px'],
            opacity: [0.7, 1, 0.7],
          }}
          transition={{
            duration: 4,
            delay: index * 0.5,
            repeat: Infinity,
          }}
        />
      ))}

      {/* Pac-Man icon */}
      <motion.div
        className="pacman-icon"
        animate={{ rotate: 360 }}
        transition={{ duration: 2, repeat: Infinity, ease: 'linear' }}
        style={{ position: 'absolute', top: '20px', right: '20px' }}
      />

      {/* Display */}
      <motion.div className="pacman-display">
        <div className="score">SCORE: {level * 100}</div>
        <div className="value">{display}</div>
        <div style={{ textAlign: 'center', color: colors.score, fontSize: '10px', marginTop: '10px' }}>
          LEVEL: {level}
        </div>
      </motion.div>

      {/* Pellets display */}
      {pellets.length > 0 && (
        <motion.div style={{ textAlign: 'center', marginBottom: '15px' }}>
          {pellets.map((pelletId) => (
            <motion.span
              key={pelletId}
              className={pelletId % 2 === 0 ? 'pellet' : 'power-pellet'}
              initial={{ scale: 0, opacity: 1 }}
              animate={{ scale: 1 }}
              exit={{ opacity: 0 }}
              transition={{ duration: 0.2 }}
            />
          ))}
        </motion.div>
      )}

      {/* Button Grid */}
      <div className={styles.buttonGrid}>
        {/* Row 1 */}
        <motion.button className="arcade-button" onClick={() => handleClear()}>
          C
        </motion.button>
        <motion.button className="arcade-button" onClick={() => toggleScientific()}>
          {scientificMode ? 'STD' : 'SCI'}
        </motion.button>
        <motion.button className="arcade-button" onClick={() => handleOperation('/')}>/</motion.button>
        <motion.button className="arcade-button" onClick={() => handleOperation('*')}>×</motion.button>

        {/* Row 2 */}
        <motion.button className="arcade-button" onClick={() => handleNumber('7')}>
          7
        </motion.button>
        <motion.button className="arcade-button" onClick={() => handleNumber('8')}>
          8
        </motion.button>
        <motion.button className="arcade-button" onClick={() => handleNumber('9')}>
          9
        </motion.button>
        <motion.button className="arcade-button" onClick={() => handleOperation('-')}>−</motion.button>

        {/* Row 3 */}
        <motion.button className="arcade-button" onClick={() => handleNumber('4')}>
          4
        </motion.button>
        <motion.button className="arcade-button" onClick={() => handleNumber('5')}>
          5
        </motion.button>
        <motion.button className="arcade-button" onClick={() => handleNumber('6')}>
          6
        </motion.button>
        <motion.button className="arcade-button" onClick={() => handleOperation('+')}>+</motion.button>

        {/* Row 4 */}
        <motion.button className="arcade-button" onClick={() => handleNumber('1')}>
          1
        </motion.button>
        <motion.button className="arcade-button" onClick={() => handleNumber('2')}>
          2
        </motion.button>
        <motion.button className="arcade-button" onClick={() => handleNumber('3')}>
          3
        </motion.button>
        <motion.button
          className="arcade-button"
          style={{ gridRow: 'span 2' }}
          onClick={() => handleEquals()}
        >
          =
        </motion.button>

        {/* Row 5 */}
        <motion.button className="arcade-button" style={{ gridColumn: 'span 2' }} onClick={() => handleNumber('0')}>
          0
        </motion.button>
        <motion.button className="arcade-button" onClick={() => handleDecimal()}>
          .
        </motion.button>

        {/* Scientific buttons - conditional render */}
        {scientificMode && (
          <>
            <motion.button className="arcade-button" onClick={() => handleScientific('sqrt')}>
              √
            </motion.button>
            <motion.button className="arcade-button" onClick={() => handleScientific('pow')}>
              x²
            </motion.button>
            <motion.button className="arcade-button" onClick={() => handleScientific('sin')}>
              sin
            </motion.button>
            <motion.button className="arcade-button" onClick={() => handleScientific('cos')}>
              cos
            </motion.button>
            <motion.button className="arcade-button" onClick={() => handleScientific('tan')}>
              tan
            </motion.button>
            <motion.button className="arcade-button" onClick={() => handleScientific('log')}>
              log
            </motion.button>
            <motion.button className="arcade-button" onClick={() => handleScientific('ln')}>
              ln
            </motion.button>
            <motion.button className="arcade-button" onClick={() => handleScientific('factorial')}>
              n!
            </motion.button>
            <motion.button className="arcade-button" onClick={() => handleScientific('reciprocal')}>
              1/x
            </motion.button>
            <motion.button className="arcade-button" onClick={() => handleScientific('percent')}>
              %
            </motion.button>
            <motion.button className="arcade-button" onClick={() => handleScientific('pi')}>
              π
            </motion.button>
            <motion.button className="arcade-button" onClick={() => handleScientific('e')}>
              e
            </motion.button>
          </>
        )}
      </div>
    </motion.div>
  );
}
