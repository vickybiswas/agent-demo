'use client';

import React, { useEffect, useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';

interface DisplayProps {
  value: string;
  memory: number;
  isError?: boolean;
}

/**
 * Display component showing calculator result with animations
 */
export const Display: React.FC<DisplayProps> = ({ value, memory, isError = false }) => {
  const [displayValue, setDisplayValue] = useState(value);
  const [key, setKey] = useState(0);

  useEffect(() => {
    if (value !== displayValue) {
      setDisplayValue(value);
      setKey((prev) => prev + 1);
    }
  }, [value, displayValue]);

  return (
    <div className="display-section">
      <AnimatePresence mode="wait">
        <motion.div
          key={key}
          className={`display ${isError ? 'error' : 'has-value'}`}
          data-testid="display"
          initial={{ opacity: 0, scale: 0.8 }}
          animate={{ opacity: 1, scale: 1 }}
          exit={{ opacity: 0, scale: 0.8 }}
          transition={{ duration: 0.3, type: 'easeOut' }}
        >
          {displayValue || '0'}
        </motion.div>
      </AnimatePresence>
      {memory !== 0 && (
        <motion.div
          className="memory-display"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.2 }}
        >
          M: {memory.toFixed(2)}
        </motion.div>
      )}
    </div>
  );
};

export default Display;
