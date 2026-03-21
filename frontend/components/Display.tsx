'use client';

import React from 'react';
import { motion } from 'framer-motion';
import { useCalculator } from '@/store/calculator';
import styles from '@/styles/calculator.module.scss';

export const Display: React.FC = () => {
  const { display, isUpsideDown, error } = useCalculator();
  const [isUpdating, setIsUpdating] = React.useState(false);

  React.useEffect(() => {
    setIsUpdating(true);
    const timeout = setTimeout(() => setIsUpdating(false), 150);
    return () => clearTimeout(timeout);
  }, [display]);

  const displayClasses = `${styles.display} ${
    isUpdating ? styles.updating : ''
  } ${isUpsideDown ? styles['upside-down'] : ''} ${
    error ? styles.errorDisplay : ''
  }`;

  return (
    <motion.div
      className={displayClasses}
      initial={{ opacity: 0.8 }}
      animate={{ opacity: 1 }}
      transition={{ duration: 0.15 }}
    >
      <motion.span
        className={styles.displayText}
        key={display}
        initial={{ scale: 0.9, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        transition={{ type: 'spring', stiffness: 300, damping: 30 }}
      >
        {display}
      </motion.span>
    </motion.div>
  );
};

export default Display;
