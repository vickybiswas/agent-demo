'use client';

import React from 'react';
import { motion } from 'framer-motion';
import styles from './Button.module.scss';

interface ButtonProps {
  label: string;
  onClick: () => void;
  variant?: 'number' | 'operation' | 'equals' | 'clear' | 'scientific';
}

export default function Button({
  label,
  onClick,
  variant = 'number'
}: ButtonProps): React.ReactNode {
  return (
    <motion.button
      className={`${styles.button} ${styles[variant]}`}
      onClick={onClick}
      whileHover={{ scale: 1.1, rotate: 2 }}
      whileTap={{ scale: 0.95 }}
      transition={{ type: 'spring', stiffness: 300 }}
    >
      {label}
    </motion.button>
  );
}
