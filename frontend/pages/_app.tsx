import type { AppProps } from 'next/app';
import '@/styles/globals.scss';
import '@/styles/calculator.scss';

/**
 * Custom App component for Next.js
 */
export default function App({ Component, pageProps }: AppProps) {
  return <Component {...pageProps} />;
}
