'use client';

import React, { useCallback } from 'react';
import { motion } from 'framer-motion';
import { playClickSound } from '@/lib/sound';

interface ButtonProps {
  label: string;
  onClick: () => void;
  className?: string;
  disabled?: boolean;
  testId?: string;
  ariaLabel?: string;
}

/**
 * Button component with animations and sound effects
 */
export const Button: React.FC<ButtonProps> = ({
  label,
  onClick,
  className = '',
  disabled = false,
  testId,
  ariaLabel,
}) => {
  const handleClick = useCallback(() => {
    if (!disabled) {
      playClickSound();
      onClick();
    }
  }, [onClick, disabled]);

  const handleKeyDown = useCallback(
    (event: React.KeyboardEvent) => {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        handleClick();
      }
    },
    [handleClick]
  );

  return (
    <motion.button
      className={`button ${className}`}
      onClick={handleClick}
      onKeyDown={handleKeyDown}
      disabled={disabled}
      data-testid={testId}
      aria-label={ariaLabel || label}
      whileHover={{ scale: disabled ? 1 : 1.05 }}
      whileTap={{ scale: 0.95 }}
      initial={{ opacity: 1 }}
      animate={{ opacity: disabled ? 0.5 : 1 }}
      transition={{ duration: 0.15, type: 'easeOut' }}
    >
      <span>{label}</span>
    </motion.button>
  );
};

export default Button;
