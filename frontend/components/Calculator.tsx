'use client';

import React, { useState, useCallback } from 'react';
import { Button } from './Button';
import { Display } from './Display';
import { calculate, scientificCalculate, getErrorMessage } from '@/lib/api';
import { playSuccessSound, playErrorSound, playEqualsSound } from '@/lib/sound';
import { motion } from 'framer-motion';

type Operation = 'add' | 'subtract' | 'multiply' | 'divide' | 'power' | 'modulo' | null;
type ScientificOperation = 'sin' | 'cos' | 'tan' | 'sqrt' | 'ln' | 'log' | 'abs' | 'factorial';

interface CalculatorState {
  display: string;
  firstNumber: number | null;
  operation: Operation;
  waitingForOperand: boolean;
  memory: number;
}

/**
 * Calculator component orchestrating all operations
 */
export const Calculator: React.FC = () => {
  const [state, setState] = useState<CalculatorState>({
    display: '0',
    firstNumber: null,
    operation: null,
    waitingForOperand: true,
    memory: 0,
  });
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [scientificMode, setScientificMode] = useState(false);
  const [angleMode, setAngleMode] = useState<'deg' | 'rad'>('deg');

  const updateDisplay = useCallback((newDisplay: string) => {
    setState((prev) => ({ ...prev, display: newDisplay }));
  }, []);

  const handleNumber = useCallback(
    (num: string) => {
      setError(null);
      setState((prev) => {
        const newDisplay =
          prev.waitingForOperand || prev.display === '0'
            ? num
            : prev.display + num;

        return {
          ...prev,
          display: newDisplay,
          waitingForOperand: false,
        };
      });
    },
    []
  );

  const handleDecimal = useCallback(() => {
    setError(null);
    setState((prev) => {
      if (prev.waitingForOperand) {
        return { ...prev, display: '0.', waitingForOperand: false };
      }
      if (prev.display.includes('.')) {
        return prev;
      }
      return { ...prev, display: prev.display + '.' };
    });
  }, []);

  const handleOperation = useCallback(
    (op: Operation) => {
      setError(null);
      const inputValue = parseFloat(state.display);

      setState((prev) => {
        let newFirstNumber = inputValue;

        if (prev.firstNumber !== null && prev.operation && !prev.waitingForOperand) {
          // Perform pending calculation
          const result = performCalculation(
            prev.firstNumber,
            inputValue,
            prev.operation
          );
          newFirstNumber = result;
          updateDisplay(String(result));
        }

        return {
          ...prev,
          firstNumber: newFirstNumber,
          operation: op,
          display: String(newFirstNumber),
          waitingForOperand: true,
        };
      });
    },
    [state.display, updateDisplay]
  );

  const performCalculation = (first: number, second: number, op: Operation): number => {
    switch (op) {
      case 'add':
        return first + second;
      case 'subtract':
        return first - second;
      case 'multiply':
        return first * second;
      case 'divide':
        return second === 0 ? 0 : first / second;
      default:
        return second;
    }
  };

  const handleEquals = useCallback(async () => {
    if (state.firstNumber === null || state.operation === null) {
      return;
    }

    setIsLoading(true);
    setError(null);

    try {
      const secondNumber = parseFloat(state.display);
      const result = await calculate(
        state.operation,
        state.firstNumber,
        secondNumber
      );

      playEqualsSound();
      playSuccessSound();

      setState((prev) => ({
        ...prev,
        display: String(result),
        firstNumber: null,
        operation: null,
        waitingForOperand: true,
      }));
    } catch (err) {
      playErrorSound();
      const errorMessage = getErrorMessage(err);
      setError(errorMessage);
      setState((prev) => ({
        ...prev,
        display: '0',
        firstNumber: null,
        operation: null,
        waitingForOperand: true,
      }));
    } finally {
      setIsLoading(false);
    }
  }, [state.firstNumber, state.operation, state.display]);

  const handleClear = useCallback(() => {
    setError(null);
    setState({
      display: '0',
      firstNumber: null,
      operation: null,
      waitingForOperand: true,
      memory: state.memory,
    });
  }, [state.memory]);

  const handleAllClear = useCallback(() => {
    setError(null);
    setState({
      display: '0',
      firstNumber: null,
      operation: null,
      waitingForOperand: true,
      memory: 0,
    });
  }, []);

  const handleMemoryAdd = useCallback(() => {
    setError(null);
    const value = parseFloat(state.display);
    setState((prev) => ({
      ...prev,
      memory: prev.memory + value,
      display: '0',
      waitingForOperand: true,
    }));
  }, [state.display]);

  const handleMemorySubtract = useCallback(() => {
    setError(null);
    const value = parseFloat(state.display);
    setState((prev) => ({
      ...prev,
      memory: prev.memory - value,
      display: '0',
      waitingForOperand: true,
    }));
  }, [state.display]);

  const handleMemoryRecall = useCallback(() => {
    setError(null);
    setState((prev) => ({
      ...prev,
      display: String(prev.memory),
      waitingForOperand: true,
    }));
  }, []);

  const handleMemoryClear = useCallback(() => {
    setError(null);
    setState((prev) => ({
      ...prev,
      memory: 0,
    }));
  }, []);

  const handleBackspace = useCallback(() => {
    setState((prev) => {
      if (prev.waitingForOperand || prev.display === '0') {
        return prev;
      }

      const newDisplay = prev.display.slice(0, -1) || '0';
      return {
        ...prev,
        display: newDisplay,
      };
    });
  }, []);

  const handleScientificOperation = useCallback(
    async (op: ScientificOperation) => {
      setError(null);
      setIsLoading(true);

      try {
        const inputValue = parseFloat(state.display);
        const result = await scientificCalculate(
          op,
          inputValue,
          angleMode === 'deg' && ['sin', 'cos', 'tan'].includes(op)
        );

        playEqualsSound();
        playSuccessSound();

        setState((prev) => ({
          ...prev,
          display: String(result),
          firstNumber: null,
          operation: null,
          waitingForOperand: true,
        }));
      } catch (err) {
        playErrorSound();
        const errorMessage = getErrorMessage(err);
        setError(errorMessage);
        setState((prev) => ({
          ...prev,
          display: '0',
          firstNumber: null,
          operation: null,
          waitingForOperand: true,
        }));
      } finally {
        setIsLoading(false);
      }
    },
    [state.display, angleMode]
  );

  const handleConstant = useCallback((value: number) => {
    setState((prev) => ({
      ...prev,
      display: String(value),
      waitingForOperand: true,
    }));
  }, []);

  return (
    <div className="calculator-wrapper">
      <div className="calculator">
        <div className="calculator-header">
          <h1>CALCULATOR</h1>
          <p>STRANGER THINGS EDITION</p>
          <motion.button
            className={`scientific-toggle ${scientificMode ? 'active' : ''}`}
            onClick={() => setScientificMode(!scientificMode)}
            whileTap={{ scale: 0.95 }}
            data-testid="scientific-toggle"
          >
            {scientificMode ? 'BASIC' : 'SCIENTIFIC'}
          </motion.button>
        </div>

        <Display value={state.display} memory={state.memory} isError={!!error} />

        {error && (
          <div className="error-message" data-testid="error-message">
            {error}
          </div>
        )}

        <div className={`buttons-grid ${scientificMode ? 'scientific' : 'basic'}`}>
          {/* Row 1: Memory Operations */}
          <Button
            label="MC"
            onClick={handleMemoryClear}
            className="memory"
            testId="memory-clear"
            ariaLabel="Memory Clear"
          />
          <Button
            label="MR"
            onClick={handleMemoryRecall}
            className="memory"
            testId="memory-recall"
            ariaLabel="Memory Recall"
          />
          <Button
            label="M+"
            onClick={handleMemoryAdd}
            className="memory"
            testId="memory-add"
            ariaLabel="Memory Add"
          />
          <Button
            label="M-"
            onClick={handleMemorySubtract}
            className="memory"
            testId="memory-subtract"
            ariaLabel="Memory Subtract"
          />

          {/* Row 2: Clear and Operations */}
          <Button
            label="C"
            onClick={handleClear}
            className="clear"
            testId="clear"
            ariaLabel="Clear"
          />
          <Button
            label="AC"
            onClick={handleAllClear}
            className="clear"
            testId="all-clear"
            ariaLabel="All Clear"
          />
          <Button
            label="÷"
            onClick={() => handleOperation('divide')}
            className="operation"
            testId="divide"
            disabled={isLoading}
            ariaLabel="Divide"
          />
          <Button
            label="×"
            onClick={() => handleOperation('multiply')}
            className="operation"
            testId="multiply"
            disabled={isLoading}
            ariaLabel="Multiply"
          />

          {/* Row 3: Numbers 7-8-9 */}
          <Button
            label="7"
            onClick={() => handleNumber('7')}
            className="number"
            testId="button-7"
            disabled={isLoading}
          />
          <Button
            label="8"
            onClick={() => handleNumber('8')}
            className="number"
            testId="button-8"
            disabled={isLoading}
          />
          <Button
            label="9"
            onClick={() => handleNumber('9')}
            className="number"
            testId="button-9"
            disabled={isLoading}
          />
          <Button
            label="-"
            onClick={() => handleOperation('subtract')}
            className="operation"
            testId="subtract"
            disabled={isLoading}
            ariaLabel="Subtract"
          />

          {/* Row 4: Numbers 4-5-6 */}
          <Button
            label="4"
            onClick={() => handleNumber('4')}
            className="number"
            testId="button-4"
            disabled={isLoading}
          />
          <Button
            label="5"
            onClick={() => handleNumber('5')}
            className="number"
            testId="button-5"
            disabled={isLoading}
          />
          <Button
            label="6"
            onClick={() => handleNumber('6')}
            className="number"
            testId="button-6"
            disabled={isLoading}
          />
          <Button
            label="+"
            onClick={() => handleOperation('add')}
            className="operation"
            testId="add"
            disabled={isLoading}
            ariaLabel="Add"
          />

          {/* Row 5: Numbers 1-2-3 */}
          <Button
            label="1"
            onClick={() => handleNumber('1')}
            className="number"
            testId="button-1"
            disabled={isLoading}
          />
          <Button
            label="2"
            onClick={() => handleNumber('2')}
            className="number"
            testId="button-2"
            disabled={isLoading}
          />
          <Button
            label="3"
            onClick={() => handleNumber('3')}
            className="number"
            testId="button-3"
            disabled={isLoading}
          />
          <Button
            label="="
            onClick={handleEquals}
            className="equals"
            testId="equals"
            disabled={isLoading}
            ariaLabel="Equals"
          />

          {/* Row 6: Decimal and Zero */}
          <Button
            label="0"
            onClick={() => handleNumber('0')}
            className="number"
            testId="button-0"
            disabled={isLoading}
          />
          <Button
            label="."
            onClick={handleDecimal}
            className="number"
            testId="decimal"
            disabled={isLoading}
            ariaLabel="Decimal"
          />
          <Button
            label="←"
            onClick={handleBackspace}
            className="number"
            testId="backspace"
            disabled={isLoading}
            ariaLabel="Backspace"
          />

          {/* Scientific Mode Buttons */}
          {scientificMode && (
            <>
              {/* Row 7: Trigonometric Functions */}
              <Button
                label="sin"
                onClick={() => handleScientificOperation('sin')}
                className="scientific"
                testId="sin"
                disabled={isLoading}
                ariaLabel="Sine"
              />
              <Button
                label="cos"
                onClick={() => handleScientificOperation('cos')}
                className="scientific"
                testId="cos"
                disabled={isLoading}
                ariaLabel="Cosine"
              />
              <Button
                label="tan"
                onClick={() => handleScientificOperation('tan')}
                className="scientific"
                testId="tan"
                disabled={isLoading}
                ariaLabel="Tangent"
              />
              <Button
                label={angleMode === 'deg' ? 'RAD' : 'DEG'}
                onClick={() => setAngleMode(angleMode === 'deg' ? 'rad' : 'deg')}
                className="scientific"
                testId="angle-mode"
                ariaLabel="Toggle Angle Mode"
              />

              {/* Row 8: Logarithmic Functions */}
              <Button
                label="ln"
                onClick={() => handleScientificOperation('ln')}
                className="scientific"
                testId="ln"
                disabled={isLoading}
                ariaLabel="Natural Logarithm"
              />
              <Button
                label="log"
                onClick={() => handleScientificOperation('log')}
                className="scientific"
                testId="log"
                disabled={isLoading}
                ariaLabel="Logarithm Base 10"
              />
              <Button
                label="√"
                onClick={() => handleScientificOperation('sqrt')}
                className="scientific"
                testId="sqrt"
                disabled={isLoading}
                ariaLabel="Square Root"
              />
              <Button
                label="π"
                onClick={() => handleConstant(Math.PI)}
                className="scientific"
                testId="pi"
                ariaLabel="Pi"
              />

              {/* Row 9: Additional Functions */}
              <Button
                label="x^y"
                onClick={() => handleOperation('power')}
                className="operation"
                testId="power"
                disabled={isLoading}
                ariaLabel="Power"
              />
              <Button
                label="!"
                onClick={() => handleScientificOperation('factorial')}
                className="scientific"
                testId="factorial"
                disabled={isLoading}
                ariaLabel="Factorial"
              />
              <Button
                label="|x|"
                onClick={() => handleScientificOperation('abs')}
                className="scientific"
                testId="abs"
                disabled={isLoading}
                ariaLabel="Absolute Value"
              />
              <Button
                label="e"
                onClick={() => handleConstant(Math.E)}
                className="scientific"
                testId="e"
                ariaLabel="Euler's Number"
              />

              {/* Row 10: Modulo */}
              <Button
                label="mod"
                onClick={() => handleOperation('modulo')}
                className="operation"
                testId="modulo"
                disabled={isLoading}
                ariaLabel="Modulo"
              />
            </>
          )}
        </div>
      </div>
    </div>
  );
};

export default Calculator;
