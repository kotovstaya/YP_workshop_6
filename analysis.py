def analyze_missing(tips):
    missing = tips.isnull().sum()
    missing_pct = (tips.isnull().mean() * 100).round(1)
    missing_df = pd.DataFrame({'Пропуски': missing, '%': missing_pct})
    missing_with = missing_df[missing_df['Пропуски'] > 0]
    if len(missing_with) > 0:
        print('Пропуски:')
        print(missing_with.sort_values('%', ascending=False))
   else:
        print('Пропусков нет')

    print(f'\nВсего строк с пропусками: {tips.isnull().any(axis=1).sum()} из {len(tips)}')

    print('\n=== Числовые столбцы ===')
    print(tips.describe().round(2))
    print('\n=== Категориальные столбцы ===')
    print(tips.describe(include=['object', 'category']))

    print(f'Всего пропусков: {tips.isnull().sum().sum()}')
    print('Обработка не требуется')

    tips['tip_pct'] = tips['tip'] / tips['total_bill'] * 100

    pairs = [('total_bill', 'tip'), ('total_bill', 'size'), ('size', 'tip')]

    for c1, c2 in pairs:
        p_corr, _ = pearsonr(tips[c1], tips[c2])
        s_corr, _ = spearmanr(tips[c1], tips[c2])
        print(f'{c1} vs {c2}:  Пирсон r={p_corr:.3f}  Спирмен p={s_corr:.3f}')

        print('Средние по дню и времени:')
    print(tips.groupby(['day', 'time'])[['tip', 'tip_pct']].mean().round(2))
    print('\nСредние по полу:')
    print(tips.groupby('sex')[['total_bill', 'tip', 'tip_pct']].mean().round(2))
