#!/usr/bin/env python3
"""
五味屋養雞記錄系統 - 收蛋大數據自動同步與統計更新腳本
支援：
1. 若 egg_stats.json 中有填寫 Google Sheets 發布之 remote_csv_url，直接從雲端拉取最新收蛋明細至「web_assets/data/egg_records.csv」！
2. 亦可直接維護或手動匯入至本機「web_assets/data/egg_records.csv」。
3. 自動計算累計產蛋數、合格蛋、破損率、平均蛋重、記錄筆數與起訖日期，更新「web_assets/data/egg_stats.json」。
"""

import os
import csv
import json
import urllib.request

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEST_CSV = os.path.join(BASE_DIR, 'web_assets', 'data', 'egg_records.csv')
STATS_JSON = os.path.join(BASE_DIR, 'web_assets', 'data', 'egg_stats.json')

def sync_and_calculate():
    remote_url = ''
    if os.path.exists(STATS_JSON):
        try:
            with open(STATS_JSON, 'r', encoding='utf-8') as f:
                old_data = json.load(f)
                remote_url = old_data.get('remote_csv_url', '')
        except Exception:
            pass

    # 1. 嘗試從遠端 Google Sheets 拉取最新 CSV（若有設定）
    downloaded_remote = False
    if remote_url and remote_url.startswith('http'):
        print(f'📡 偵測到遠端 Google Sheets CSV 網址，正在下載最新紀錄：{remote_url}')
        try:
            req = urllib.request.Request(remote_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=10) as resp:
                content = resp.read().decode('utf-8')
                with open(DEST_CSV, 'w', encoding='utf-8') as f:
                    f.write(content)
                downloaded_remote = True
                print('✅ 成功從 Google Sheets 同步最新收蛋紀錄！')
        except Exception as e:
            print(f'⚠️ 遠端下載失敗（{e}），改由本機 CSV 進行統計運算。')

    if not os.path.exists(DEST_CSV):
        print('❌ 找不到收蛋記錄 CSV 檔案：', DEST_CSV)
        return

    # 2. 解析 CSV 並重新統計
    rows = []
    with open(DEST_CSV, 'r', encoding='utf-8', errors='ignore') as f:
        reader = csv.DictReader(f)
        for r in reader:
            rows.append(r)

    total_records = len(rows)
    total_eggs = sum(int(r.get('總收蛋數(顆)') or 0) for r in rows)
    qualified_eggs = sum(int(r.get('合格蛋(顆)') or 0) for r in rows)
    broken_eggs = sum(int(r.get('破損蛋(顆)') or 0) for r in rows)
    dirty_eggs = sum(int(r.get('地板蛋/沾糞蛋(顆)') or 0) for r in rows)
    total_weight = sum(float(r.get('總蛋重(g)') or 0) for r in rows if float(r.get('總蛋重(g)') or 0) > 0)

    avg_weight = round(total_weight / total_eggs, 1) if total_eggs else 0
    broken_rate = round((broken_eggs / total_eggs) * 100, 1) if total_eggs else 0

    dates = sorted(list(set(r.get('日期', '').strip() for r in rows if r.get('日期', '').strip())))
    start_date = dates[0] if dates else '2026-08-10'
    end_date = dates[-1] if dates else ''

    stats = {
        'total_eggs': total_eggs,
        'qualified_eggs': qualified_eggs,
        'broken_eggs': broken_eggs,
        'dirty_eggs': dirty_eggs,
        'total_records': total_records,
        'avg_weight': avg_weight,
        'broken_rate': f'{broken_rate}%',
        'laying_rate': '70%~80%',
        'start_date': start_date,
        'end_date': end_date,
        'period_text': f'記錄至 {end_date}（全歷程累計 {total_eggs} 顆）',
        'remote_csv_url': remote_url
    }

    with open(STATS_JSON, 'w', encoding='utf-8') as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    print('📊 統計結果已成功更新至 egg_stats.json：')
    print(f'   • 累計收蛋總數：{total_eggs} 顆')
    print(f'   • 合格蛋數：{qualified_eggs} 顆')
    print(f'   • 破損蛋數：{broken_eggs} 顆（破損率：{broken_rate}%）')
    print(f'   • 平均單蛋重：{avg_weight} g')
    print(f'   • 總值日記錄：{total_records} 筆（{start_date} ~ {end_date}）')

if __name__ == '__main__':
    sync_and_calculate()
