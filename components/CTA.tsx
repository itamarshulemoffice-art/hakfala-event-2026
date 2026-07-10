import Link from "next/link";
import { CHECKOUT_URL } from "@/lib/site";
import { Icon } from "./Icons";

export function CTA({
  children,
  className = "",
  full = false,
}: {
  children: React.ReactNode;
  className?: string;
  full?: boolean;
}) {
  const isAnchor = CHECKOUT_URL.startsWith("#");
  const cls = `btn-gold ${full ? "w-full" : ""} ${className}`;
  const inner = (
    <>
      <Icon name="arrow" width={20} height={20} style={{ transform: "scaleX(-1)" }} />
      <span>{children}</span>
    </>
  );
  if (isAnchor) {
    return (
      <a href={CHECKOUT_URL} className={cls}>
        {inner}
      </a>
    );
  }
  return (
    <Link href={CHECKOUT_URL} className={cls} target="_blank" rel="noopener">
      {inner}
    </Link>
  );
}
