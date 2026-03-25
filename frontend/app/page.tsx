import Calculator from "@/components/Calculator";
import styles from "./page.module.scss";

export default function Home() {
  return (
    <main className={styles.main}>
      <Calculator />
    </main>
  );
}
