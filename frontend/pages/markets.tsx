import { useEffect, useState } from "react";

export default function Markets() {
    const [data, setData] = useState<any>(null);

    useEffect(() => {
        fetch("http://127.0.0.1:8000/market/price?symbol=HDFCBANK.NS")
            .then(res => res.json())
            .then(setData);
    }, []);

    return (
        <div className="p-6">
            <h1 className="text-xl font-semibold mb-4">Markets</h1>
            {data && (
                <div className="bg-zinc-900 p-4 rounded">
                    <p>Price: ₹{data.price}</p>
                    <p>Change: {data.change}</p>
                </div>
            )}
        </div>
    );
}
