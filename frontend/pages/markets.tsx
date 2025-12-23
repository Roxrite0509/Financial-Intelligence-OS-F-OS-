import { useEffect, useState } from "react";
import axios from "axios";

type Bank = {
    symbol: string;
    price: number;
    return_pct: number;
    volatility: number;
};

export default function Markets() {
    const [banks, setBanks] = useState<Bank[]>([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        axios
            .get("http://127.0.0.1:8000/market/compare?symbols=SBIN.NS,HDFCBANK.NS")
            .then(res => setBanks(res.data))
            .finally(() => setLoading(false));
    }, []);

    if (loading) return <p>Loading…</p>;

    return (
        <div>
            <h2 className="accent">Bank Comparison</h2>
            {banks.map(b => (
                <div className="card" key={b.symbol}>
                    <h3>{b.symbol}</h3>
                    <p>Price: ₹{b.price}</p>
                    <p>Return: {b.return_pct}%</p>
                    <p>Volatility: {b.volatility}%</p>
                </div>
            ))}
        </div>
    );
}
