'use client';

import React from 'react';
import { motion } from 'framer-motion';
import styles from '@/styles/calculator.module.scss';

interface ButtonProps {
  label: string;
  onClick: () => void;
  type?: 'number' | 'operation' | 'clear' | 'equals';
  disabled?: boolean;
  dataButton?: string;
}

export const Button: React.FC<ButtonProps> = ({
  label,
  onClick,
  type = 'number',
  disabled = false,
  dataButton,
}) => {
  const handleClick = () => {
    onClick();
  };

  const buttonClass = `${styles.button} ${
    type === 'operation' ? styles.operation : ''
  } ${type === 'clear' ? styles.clear : ''}`;

  return (
    <motion.button
      className={buttonClass}
      onClick={handleClick}
      disabled={disabled}
      data-button={dataButton}
      type="button"
      whileHover={{ scale: 1.05 }}
      whileTap={{ scale: 0.95 }}
      transition={{ type: 'spring', stiffness: 400, damping: 17 }}
    >
      {label}
    </motion.button>
  );
};

export default Button;
