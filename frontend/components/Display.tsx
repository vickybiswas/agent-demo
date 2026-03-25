"use client";

import { motion } from "framer-motion";
import styles from "./Display.module.scss";

interface DisplayProps {
  value: string;
}

export default function Display({ value }: DisplayProps) {
  return (
    <motion.div
      className={styles.display}
      initial={{ opacity: 0, y: -20 }}
      animate={{ opacity: 1, y: 0 }}
    >
      <motion.p
        key={value}
        initial={{ scale: 0.8, opacity: 0 }}
        animate={{ scale: 1, opacity: 1 }}
        transition={{ duration: 0.2 }}
      >
        {value}
      </motion.p>
    </motion.div>
  );
}
