'use client';

import React from 'react';
import styles from './Display.module.scss';

interface DisplayProps {
  display: string;
  result: string;
}

export default function Display({ display, result }: DisplayProps): React.ReactNode {
  return (
    <div className={styles.displayContainer}>
      <div className={styles.inputLine} data-testid="inputLine">
        {display || '0'}
      </div>
      <div className={styles.resultLine} data-testid="resultLine">
        {result || ''}
      </div>
    </div>
  );
}
