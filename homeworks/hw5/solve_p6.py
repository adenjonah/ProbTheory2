"""
Problem 6: Stock Returns
Using Yahoo Finance data:
1. Download SP500 (^GSPC) and VIX (^VIX) data from Nov 10, 2015 to Nov 10, 2025
2. Calculate daily returns for both series
3. Estimate mean, std, and correlation
4. Calculate empirical and theoretical P(SP500 returns < 3%)
"""
import numpy as np
import pandas as pd
import yfinance as yf
from scipy import stats
import matplotlib.pyplot as plt

print("="*60)
print("Problem 6: Stock Returns Analysis")
print("="*60)

# Download data
start_date = "2015-11-10"
end_date = "2025-11-10"

print(f"\nDownloading data from {start_date} to {end_date}...")

try:
    sp500 = yf.download("^GSPC", start=start_date, end=end_date, progress=False, auto_adjust=True)
    vix = yf.download("^VIX", start=start_date, end=end_date, progress=False, auto_adjust=True)
    
    print(f"SP500 data: {len(sp500)} days")
    print(f"VIX data: {len(vix)} days")
    
    # Calculate daily returns (percent change)
    # Handle both single-level and multi-level column DataFrames
    if isinstance(sp500.columns, pd.MultiIndex):
        sp500_close = sp500['Close'].iloc[:, 0] if len(sp500['Close'].shape) > 1 else sp500['Close']
    else:
        sp500_close = sp500['Close']
    
    if isinstance(vix.columns, pd.MultiIndex):
        vix_close = vix['Close'].iloc[:, 0] if len(vix['Close'].shape) > 1 else vix['Close']
    else:
        vix_close = vix['Close']
    
    sp500_returns = sp500_close.pct_change().dropna()
    vix_returns = vix_close.pct_change().dropna()
    
    # Align dates (keep only common dates)
    common_dates = sp500_returns.index.intersection(vix_returns.index)
    sp500_returns = sp500_returns.loc[common_dates]
    vix_returns = vix_returns.loc[common_dates]
    
    print(f"Common trading days: {len(sp500_returns)}")
    
    # Compute statistics
    print("\n" + "="*60)
    print("STATISTICS:")
    print("="*60)
    
    sp500_mean = sp500_returns.mean()
    sp500_std = sp500_returns.std()
    
    vix_mean = vix_returns.mean()
    vix_std = vix_returns.std()
    
    correlation = sp500_returns.corr(vix_returns)
    
    print(f"\nSP500 Returns:")
    print(f"  Mean: {sp500_mean:.10f} ({sp500_mean*100:.6f}%)")
    print(f"  Std:  {sp500_std:.10f} ({sp500_std*100:.6f}%)")
    
    print(f"\nVIX Returns:")
    print(f"  Mean: {vix_mean:.10f} ({vix_mean*100:.6f}%)")
    print(f"  Std:  {vix_std:.10f} ({vix_std*100:.6f}%)")
    
    print(f"\nCorrelation between SP500 and VIX returns:")
    print(f"  ρ = {correlation:.10f}")
    
    # P(SP500 returns < 3%) = P(SP500 returns < 0.03)
    threshold = 0.03
    
    print("\n" + "="*60)
    print(f"PROBABILITY THAT SP500 RETURNS < {threshold*100}%:")
    print("="*60)
    
    # Empirical probability
    prob_empirical = (sp500_returns < threshold).mean()
    
    print(f"\nEmpirical probability:")
    print(f"  Number of days with returns < {threshold*100}%: {(sp500_returns < threshold).sum()}")
    print(f"  Total days: {len(sp500_returns)}")
    print(f"  P(returns < {threshold*100}%) = {prob_empirical:.10f}")
    
    # Theoretical probability (assuming normal distribution)
    z_score = (threshold - sp500_mean) / sp500_std
    prob_theoretical = stats.norm.cdf(z_score)
    
    print(f"\nTheoretical probability (fitted normal):")
    print(f"  z-score = ({threshold} - {sp500_mean:.10f}) / {sp500_std:.10f}")
    print(f"          = {z_score:.10f}")
    print(f"  P(returns < {threshold*100}%) = Φ({z_score:.10f})")
    print(f"                             = {prob_theoretical:.10f}")
    
    print(f"\nDifference: {abs(prob_empirical - prob_theoretical):.10f}")
    
    # Additional statistics
    print("\n" + "="*60)
    print("ADDITIONAL STATISTICS:")
    print("="*60)
    
    print(f"\nSP500 Returns Percentiles:")
    for p in [1, 5, 10, 25, 50, 75, 90, 95, 99]:
        percentile = np.percentile(sp500_returns, p)
        print(f"  {p}th percentile: {percentile:.6f} ({percentile*100:.4f}%)")
    
    print(f"\nVIX Returns Percentiles:")
    for p in [1, 5, 10, 25, 50, 75, 90, 95, 99]:
        percentile = np.percentile(vix_returns, p)
        print(f"  {p}th percentile: {percentile:.6f} ({percentile*100:.4f}%)")
    
    # Normality tests
    print("\n" + "="*60)
    print("NORMALITY TESTS:")
    print("="*60)
    
    # Shapiro-Wilk test (use sample if too many observations)
    if len(sp500_returns) > 5000:
        np.random.seed(123456)
        sample_indices = np.random.choice(len(sp500_returns), 5000, replace=False)
        sp500_sample = sp500_returns.iloc[sample_indices]
        stat, p_value = stats.shapiro(sp500_sample)
        print(f"\nSP500 Returns Shapiro-Wilk test (n=5000 sample):")
    else:
        stat, p_value = stats.shapiro(sp500_returns)
        print(f"\nSP500 Returns Shapiro-Wilk test:")
    
    print(f"  Statistic: {stat:.6f}")
    print(f"  p-value: {p_value:.6e}")
    print(f"  Normal (p > 0.05)? {p_value > 0.05}")
    
    # Skewness and kurtosis
    skewness = stats.skew(sp500_returns)
    kurtosis_val = stats.kurtosis(sp500_returns)
    
    print(f"\nSP500 Returns Distribution Shape:")
    print(f"  Skewness: {skewness:.6f} (normal = 0)")
    print(f"  Excess Kurtosis: {kurtosis_val:.6f} (normal = 0)")
    
    # Create histogram comparison plot
    print("\n" + "="*60)
    print("CREATING PLOTS:")
    print("="*60)
    
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    
    # Plot 1: SP500 returns histogram with fitted normal
    ax = axes[0, 0]
    ax.hist(sp500_returns, bins=100, density=True, alpha=0.7, edgecolor='black', label='Empirical')
    x = np.linspace(sp500_returns.min(), sp500_returns.max(), 1000)
    ax.plot(x, stats.norm.pdf(x, sp500_mean, sp500_std), 'r-', linewidth=2, label='Fitted Normal')
    ax.axvline(threshold, color='green', linestyle='--', linewidth=2, label=f'Threshold = {threshold*100}%')
    ax.set_xlabel('Daily Returns', fontsize=12)
    ax.set_ylabel('Density', fontsize=12)
    ax.set_title('SP500 Daily Returns Distribution', fontsize=14, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    
    # Plot 2: Q-Q plot for SP500
    ax = axes[0, 1]
    stats.probplot(sp500_returns, dist="norm", plot=ax)
    ax.set_title('SP500 Returns Q-Q Plot', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    # Plot 3: VIX returns histogram with fitted normal
    ax = axes[1, 0]
    ax.hist(vix_returns, bins=100, density=True, alpha=0.7, edgecolor='black', label='Empirical')
    x_vix = np.linspace(vix_returns.min(), vix_returns.max(), 1000)
    ax.plot(x_vix, stats.norm.pdf(x_vix, vix_mean, vix_std), 'r-', linewidth=2, label='Fitted Normal')
    ax.set_xlabel('Daily Returns', fontsize=12)
    ax.set_ylabel('Density', fontsize=12)
    ax.set_title('VIX Daily Returns Distribution', fontsize=14, fontweight='bold')
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)
    
    # Plot 4: Scatter plot of SP500 vs VIX returns
    ax = axes[1, 1]
    ax.scatter(sp500_returns, vix_returns, alpha=0.3, s=5)
    ax.set_xlabel('SP500 Returns', fontsize=12)
    ax.set_ylabel('VIX Returns', fontsize=12)
    ax.set_title(f'SP500 vs VIX Returns (ρ = {correlation:.4f})', fontsize=14, fontweight='bold')
    ax.grid(True, alpha=0.3)
    
    # Add correlation line
    z = np.polyfit(sp500_returns, vix_returns, 1)
    p = np.poly1d(z)
    x_line = np.array([sp500_returns.min(), sp500_returns.max()])
    ax.plot(x_line, p(x_line), "r--", linewidth=2, label=f'y = {z[0]:.2f}x + {z[1]:.4f}')
    ax.legend(fontsize=10)
    
    plt.tight_layout()
    plt.savefig('figures/P6_stock_returns_analysis.png', dpi=300, bbox_inches='tight')
    print("Saved figure: figures/P6_stock_returns_analysis.png")
    plt.close()
    
    # Save data summary
    print("\n" + "="*60)
    print("SAVING SUMMARY:")
    print("="*60)
    
    summary_df = pd.DataFrame({
        'Statistic': ['Mean', 'Std Dev', 'Min', 'Max', '25th %ile', 'Median', '75th %ile', 
                      'Skewness', 'Kurtosis', 'Count'],
        'SP500': [sp500_mean, sp500_std, sp500_returns.min(), sp500_returns.max(),
                  np.percentile(sp500_returns, 25), np.median(sp500_returns),
                  np.percentile(sp500_returns, 75), skewness, kurtosis_val, len(sp500_returns)],
        'VIX': [vix_mean, vix_std, vix_returns.min(), vix_returns.max(),
                np.percentile(vix_returns, 25), np.median(vix_returns),
                np.percentile(vix_returns, 75), stats.skew(vix_returns), 
                stats.kurtosis(vix_returns), len(vix_returns)]
    })
    
    summary_df.to_csv('artifacts/P6_summary_statistics.csv', index=False)
    print("Saved: artifacts/P6_summary_statistics.csv")
    
    print("\n" + "="*60)
    print("FINAL ANSWERS:")
    print("="*60)
    print(f"\nSP500 Returns:")
    print(f"  Mean: {sp500_mean*100:.6f}%")
    print(f"  Standard Deviation: {sp500_std*100:.6f}%")
    
    print(f"\nVIX Returns:")
    print(f"  Mean: {vix_mean*100:.6f}%")
    print(f"  Standard Deviation: {vix_std*100:.6f}%")
    
    print(f"\nCorrelation: {correlation:.6f}")
    
    print(f"\nP(SP500 returns < 3%):")
    print(f"  Empirical: {prob_empirical:.6f} ({prob_empirical*100:.4f}%)")
    print(f"  Theoretical (normal): {prob_theoretical:.6f} ({prob_theoretical*100:.4f}%)")
    
except Exception as e:
    print(f"\nError occurred: {e}")
    print("\nNote: This problem requires internet connection to download Yahoo Finance data.")
    print("If data download fails, check:")
    print("1. Internet connection")
    print("2. Yahoo Finance service availability")
    print("3. Ticker symbols are correct (^GSPC, ^VIX)")

