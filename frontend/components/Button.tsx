"use client";

import { motion } from "framer-motion";
import styles from "./Button.module.scss";

interface ButtonProps {
  children: React.ReactNode;
  onClick: () => void;
  wide?: boolean;
}

export default function Button({ children, onClick, wide }: ButtonProps) {
  return (
    <motion.button
      className={`${styles.button} ${wide ? styles.wide : ""}`}
      onClick={onClick}
      whileTap={{ scale: 0.95 }}
      whileHover={{ scale: 1.05 }}
    >
      {children}
    </motion.button>
  );
}
