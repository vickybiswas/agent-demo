"use client";

import { useState, useCallback } from "react";
import { motion } from "framer-motion";
import Display from "./Display";
import Button from "./Button";
import styles from "./Calculator.module.scss";

type Operation = "+" | "-" | "*" | "/";

const API_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8004";

// Sound effects manager
const playSound = (type: "click" | "result" | "scientific" | "error") => {
  if (typeof window === "undefined") return;

  const audioContext = new (window.AudioContext || (window as any).webkitAudioContext)();
  const oscillator = audioContext.createOscillator();
  const gainNode = audioContext.createGain();

  oscillator.connect(gainNode);
  gainNode.connect(audioContext.destination);

  switch (type) {
    case "click":
      oscillator.frequency.value = 800;
      gainNode.gain.setValueAtTime(0.1, audioContext.currentTime);
      gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.1);
      oscillator.start(audioContext.currentTime);
      oscillator.stop(audioContext.currentTime + 0.1);
      break;
    case "result":
      oscillator.frequency.value = 1200;
      gainNode.gain.setValueAtTime(0.15, audioContext.currentTime);
      gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.15);
      oscillator.start(audioContext.currentTime);
      oscillator.stop(audioContext.currentTime + 0.15);
      break;
    case "scientific":
      oscillator.frequency.value = 1500;
      gainNode.gain.setValueAtTime(0.12, audioContext.currentTime);
      gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.2);
      oscillator.start(audioContext.currentTime);
      oscillator.stop(audioContext.currentTime + 0.2);
      break;
  }
};

export default function Calculator() {
  const [display, setDisplay] = useState<string>("0");
  const [previousValue, setPreviousValue] = useState<number | null>(null);
  const [operation, setOperation] = useState<Operation | null>(null);
  const [waitingForNewValue, setWaitingForNewValue] = useState<boolean>(false);
  const [scientificMode, setScientificMode] = useState<boolean>(false);

  const handleNumber = useCallback(
    (num: string): void => {
      playSound("click");
      setDisplay((prev) =>
        waitingForNewValue ? num : prev === "0" ? num : prev + num,
      );
      setWaitingForNewValue(false);
    },
    [waitingForNewValue],
  );

  const handleOperation = useCallback(
    (op: Operation): void => {
      playSound("click");
      const currentValue = parseFloat(display);

      if (previousValue !== null && operation && !waitingForNewValue) {
        const result = calculate(previousValue, currentValue, operation);
        setDisplay(String(result));
        setPreviousValue(result);
      } else {
        setPreviousValue(currentValue);
      }

      setOperation(op);
      setWaitingForNewValue(true);
    },
    [display, previousValue, operation, waitingForNewValue],
  );

  const handleScientific = useCallback(
    async (func: string): Promise<void> => {
      playSound("scientific");
      const currentValue = parseFloat(display);
      let result: number;

      try {
        const response = await fetch(
          `${API_URL}/${func}?num=${currentValue}`,
        );
        const data = await response.json();
        result = data.result;
      } catch (error) {
        result = 0;
      }

      setDisplay(String(result));
      playSound("result");
      setWaitingForNewValue(true);
    },
    [display],
  );

  const handleEquals = useCallback((): void => {
    if (previousValue !== null && operation) {
      const result = calculate(previousValue, parseFloat(display), operation);
      setDisplay(String(result));
      playSound("result");
      setPreviousValue(null);
      setOperation(null);
      setWaitingForNewValue(true);
    }
  }, [display, previousValue, operation]);

  const handleClear = useCallback((): void => {
    playSound("click");
    setDisplay("0");
    setPreviousValue(null);
    setOperation(null);
    setWaitingForNewValue(false);
  }, []);

  const toggleScientific = useCallback((): void => {
    playSound("scientific");
    setScientificMode(!scientificMode);
  }, [scientificMode]);

  const calculate = (prev: number, curr: number, op: Operation): number => {
    switch (op) {
      case "+":
        return prev + curr;
      case "-":
        return prev - curr;
      case "*":
        return prev * curr;
      case "/":
        return curr === 0 ? 0 : prev / curr;
      default:
        return curr;
    }
  };

  return (
    <motion.div
      className={styles.calculator}
      initial={{ opacity: 0, scale: 0.9 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.3 }}
    >
      <motion.div
        className={styles.modeIndicator}
        animate={{
          background: scientificMode
            ? "rgba(0, 212, 255, 0.3)"
            : "rgba(255, 107, 107, 0.3)",
        }}
      >
        {scientificMode ? "Scientific" : "Basic"}
      </motion.div>

      <Display value={display} />

      <motion.button
        className={styles.modeToggle}
        onClick={toggleScientific}
        whileHover={{ scale: 1.05 }}
        whileTap={{ scale: 0.95 }}
      >
        {scientificMode ? "← Basic" : "Scientific →"}
      </motion.button>

      <div className={styles.buttons}>
        <Button onClick={handleClear}>C</Button>
        <Button onClick={() => handleOperation("/")}>/</Button>
        <Button onClick={() => handleOperation("*")}>*</Button>
        {scientificMode && <Button onClick={() => handleScientific("sqrt")}>√</Button>}

        <Button onClick={() => handleNumber("7")}>7</Button>
        <Button onClick={() => handleNumber("8")}>8</Button>
        <Button onClick={() => handleNumber("9")}>9</Button>
        <Button onClick={() => handleOperation("-")}>-</Button>

        <Button onClick={() => handleNumber("4")}>4</Button>
        <Button onClick={() => handleNumber("5")}>5</Button>
        <Button onClick={() => handleNumber("6")}>6</Button>
        <Button onClick={() => handleOperation("+")}>+</Button>

        <Button onClick={() => handleNumber("1")}>1</Button>
        <Button onClick={() => handleNumber("2")}>2</Button>
        <Button onClick={() => handleNumber("3")}>3</Button>
        <Button onClick={handleEquals}>=</Button>

        <Button onClick={() => handleNumber("0")} wide>
          0
        </Button>
        <Button onClick={() => handleNumber(".")}>.</Button>

        {scientificMode && (
          <>
            <Button onClick={() => handleScientific("sin")}>sin</Button>
            <Button onClick={() => handleScientific("cos")}>cos</Button>
            <Button onClick={() => handleScientific("tan")}>tan</Button>
            <Button onClick={() => handleScientific("log")}>log</Button>
            <Button onClick={() => handleScientific("factorial")}>!</Button>
            <Button onClick={() => handleScientific("pi")}>π</Button>
          </>
        )}
      </div>
    </motion.div>
  );
}
