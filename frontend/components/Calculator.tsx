'use client';

import React, { useState, useCallback } from 'react';
import { motion } from 'framer-motion';
import Button from './Button';
import Display from './Display';
import styles from './Calculator.module.scss';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8004';

interface CalculatorState {
  display: string;
  result: string;
  operation: string | null;
  waitingForOperand: boolean;
  firstOperand: number | null;
  operationName: string;
}

export default function Calculator(): React.ReactNode {
  const [state, setState] = useState<CalculatorState>({
    display: '',
    result: '',
    operation: null,
    waitingForOperand: false,
    firstOperand: null,
    operationName: '',
  });

  const handleNumberClick = useCallback((num: string) => {
    setState((prevState) => {
      if (prevState.waitingForOperand) {
        return {
          ...prevState,
          display: String(num),
          waitingForOperand: false,
        };
      }
      return {
        ...prevState,
        display: prevState.display + num,
      };
    });
  }, []);

  const handleBinaryOperation = useCallback((op: string, name: string) => {
    setState((prevState) => {
      const currentValue = parseFloat(prevState.display) || 0;

      if (prevState.firstOperand === null) {
        return {
          ...prevState,
          firstOperand: currentValue,
          operation: op,
          operationName: name,
          waitingForOperand: true,
        };
      }

      if (prevState.operation && !prevState.waitingForOperand) {
        return {
          ...prevState,
          firstOperand: currentValue,
          operation: op,
          operationName: name,
          waitingForOperand: true,
        };
      }

      return {
        ...prevState,
        operation: op,
        operationName: name,
        waitingForOperand: true,
      };
    });
  }, []);

  const handleUnaryOperation = useCallback((endpoint: string, name: string) => {
    setState((prevState) => {
      const value = parseFloat(prevState.display) || 0;

      fetch(`${API_URL}/${endpoint}?num1=${value}`)
        .then((response) => {
          if (!response.ok) {
            return response.json().then((data) => {
              throw new Error(data.detail || `Error in ${name}`);
            });
          }
          return response.json();
        })
        .then((data) => {
          setState((s) => ({
            ...s,
            result: String(data.result),
            display: '',
            operation: null,
            waitingForOperand: true,
            firstOperand: null,
            operationName: '',
          }));
        })
        .catch((error) => {
          setState((s) => ({
            ...s,
            result: String(error.message),
            display: '',
            operation: null,
            waitingForOperand: true,
            firstOperand: null,
            operationName: '',
          }));
        });

      return prevState;
    });
  }, []);

  const handleEquals = useCallback(() => {
    setState((prevState) => {
      if (!prevState.operation || prevState.firstOperand === null) {
        return prevState;
      }

      const secondOperand = parseFloat(prevState.display) || 0;
      const operationMap: Record<string, string> = {
        '+': 'add',
        '-': 'subtract',
        '*': 'multiply',
        '/': 'divide',
        '^': 'power',
      };

      const endpoint = operationMap[prevState.operation];

      if (endpoint) {
        fetch(
          `${API_URL}/${endpoint}?num1=${prevState.firstOperand}&num2=${secondOperand}`
        )
          .then((response) => {
            if (!response.ok) {
              return response.json().then((data) => {
                throw new Error(data.detail || 'Error');
              });
            }
            return response.json();
          })
          .then((data) => {
            setState((s) => ({
              ...s,
              result: String(data.result),
              display: '',
              operation: null,
              waitingForOperand: true,
              firstOperand: null,
              operationName: '',
            }));
          })
          .catch((error) => {
            setState((s) => ({
              ...s,
              result: String(error.message),
              display: '',
              operation: null,
              waitingForOperand: true,
              firstOperand: null,
              operationName: '',
            }));
          });
      }

      return prevState;
    });
  }, []);

  const handleClear = useCallback(() => {
    setState({
      display: '',
      result: '',
      operation: null,
      waitingForOperand: false,
      firstOperand: null,
      operationName: '',
    });
  }, []);

  return (
    <motion.div
      className={styles.calculatorWrapper}
      initial={{ opacity: 0, scale: 0.9 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.5 }}
    >
      <div className={styles.calculator}>
        <h1 className={styles.title}>STRANGER THINGS</h1>
        <h2 className={styles.subtitle}>CALCULATOR</h2>

        <Display display={state.display} result={state.result} />

        <div className={styles.buttonGrid}>
          <Button
            label="C"
            onClick={handleClear}
            variant="clear"
          />
          <Button
            label="/"
            onClick={() => handleBinaryOperation('/', 'divide')}
            variant="operation"
          />
          <Button
            label="*"
            onClick={() => handleBinaryOperation('*', 'multiply')}
            variant="operation"
          />

          <Button label="7" onClick={() => handleNumberClick('7')} variant="number" />
          <Button label="8" onClick={() => handleNumberClick('8')} variant="number" />
          <Button label="9" onClick={() => handleNumberClick('9')} variant="number" />
          <Button
            label="-"
            onClick={() => handleBinaryOperation('-', 'subtract')}
            variant="operation"
          />

          <Button label="4" onClick={() => handleNumberClick('4')} variant="number" />
          <Button label="5" onClick={() => handleNumberClick('5')} variant="number" />
          <Button label="6" onClick={() => handleNumberClick('6')} variant="number" />
          <Button
            label="+"
            onClick={() => handleBinaryOperation('+', 'add')}
            variant="operation"
          />

          <Button label="1" onClick={() => handleNumberClick('1')} variant="number" />
          <Button label="2" onClick={() => handleNumberClick('2')} variant="number" />
          <Button label="3" onClick={() => handleNumberClick('3')} variant="number" />
          <Button
            label="="
            onClick={handleEquals}
            variant="equals"
          />

          <Button label="0" onClick={() => handleNumberClick('0')} variant="number" />
          <Button label="." onClick={() => handleNumberClick('.')} variant="number" />
        </div>

        <div className={styles.scientificSection}>
          <h3 className={styles.sectionTitle}>Scientific Operations</h3>
          <div className={styles.scientificGrid}>
            <Button
              label="√"
              onClick={() => handleUnaryOperation('sqrt', 'sqrt')}
              variant="scientific"
            />
            <Button
              label="^"
              onClick={() => handleBinaryOperation('^', 'power')}
              variant="scientific"
            />
            <Button
              label="sin"
              onClick={() => handleUnaryOperation('sin', 'sin')}
              variant="scientific"
            />
            <Button
              label="cos"
              onClick={() => handleUnaryOperation('cos', 'cos')}
              variant="scientific"
            />
            <Button
              label="tan"
              onClick={() => handleUnaryOperation('tan', 'tan')}
              variant="scientific"
            />
            <Button
              label="log"
              onClick={() => handleUnaryOperation('log', 'log')}
              variant="scientific"
            />
            <Button
              label="ln"
              onClick={() => handleUnaryOperation('ln', 'ln')}
              variant="scientific"
            />
            <Button
              label="n!"
              onClick={() => handleUnaryOperation('factorial', 'factorial')}
              variant="scientific"
            />
          </div>
        </div>
      </div>
    </motion.div>
  );
}
