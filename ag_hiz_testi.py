
import threading
import customtkinter as ctk

try:
    import speedtest
except ImportError:
    speedtest = None



ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

APP_WIDTH = 560
APP_HEIGHT = 520


class SpeedTestApp(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Ağ Hız Testi")
        self.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")
        self.resizable(False, False)

        self._build_ui()

    def _build_ui(self):
     
        title_label = ctk.CTkLabel(
            self,
            text="🌐  Ağ Hız Testi",
            font=ctk.CTkFont(size=28, weight="bold"),
        )
        title_label.pack(pady=(25, 5))

        subtitle_label = ctk.CTkLabel(
            self,
            text="İnternet bağlantı hızınızı ölçün",
            font=ctk.CTkFont(size=13),
            text_color="#8a8a8a",
        )
        subtitle_label.pack(pady=(0, 20))

      
        cards_frame = ctk.CTkFrame(self, fg_color="transparent")
        cards_frame.pack(pady=10, padx=20, fill="x")
        cards_frame.grid_columnconfigure(0, weight=1)
        cards_frame.grid_columnconfigure(1, weight=1)

        
        self.download_card = ctk.CTkFrame(
            cards_frame, corner_radius=15, fg_color="#1f6aa5"
        )
        self.download_card.grid(row=0, column=0, padx=10, sticky="nsew")

        ctk.CTkLabel(
            self.download_card,
            text="⬇  İNDİRME",
            font=ctk.CTkFont(size=14, weight="bold"),
        ).pack(pady=(18, 5))

        self.download_value_label = ctk.CTkLabel(
            self.download_card,
            text="-- Mbps",
            font=ctk.CTkFont(size=30, weight="bold"),
        )
        self.download_value_label.pack(pady=(0, 18))

        
        self.upload_card = ctk.CTkFrame(
            cards_frame, corner_radius=15, fg_color="#2e7d32"
        )
        self.upload_card.grid(row=0, column=1, padx=10, sticky="nsew")

        ctk.CTkLabel(
            self.upload_card,
            text="⬆  YÜKLEME",
            font=ctk.CTkFont(size=14, weight="bold"),
        ).pack(pady=(18, 5))

        self.upload_value_label = ctk.CTkLabel(
            self.upload_card,
            text="-- Mbps",
            font=ctk.CTkFont(size=30, weight="bold"),
        )
        self.upload_value_label.pack(pady=(0, 18))

       
        info_frame = ctk.CTkFrame(self, corner_radius=15)
        info_frame.pack(pady=20, padx=20, fill="x")

        info_frame.grid_columnconfigure(0, weight=1)
        info_frame.grid_columnconfigure(1, weight=1)

        ping_title = ctk.CTkLabel(
            info_frame, text="PİNG", font=ctk.CTkFont(size=12, weight="bold"),
            text_color="#8a8a8a"
        )
        ping_title.grid(row=0, column=0, pady=(15, 0))

        self.ping_value_label = ctk.CTkLabel(
            info_frame, text="-- ms", font=ctk.CTkFont(size=18, weight="bold")
        )
        self.ping_value_label.grid(row=1, column=0, pady=(0, 15))

        server_title = ctk.CTkLabel(
            info_frame, text="SUNUCU / LOKASYON",
            font=ctk.CTkFont(size=12, weight="bold"),
            text_color="#8a8a8a"
        )
        server_title.grid(row=0, column=1, pady=(15, 0))

        self.server_value_label = ctk.CTkLabel(
            info_frame, text="--", font=ctk.CTkFont(size=14, weight="bold"),
            wraplength=220, justify="center"
        )
        self.server_value_label.grid(row=1, column=1, pady=(0, 15), padx=10)

        
        self.status_label = ctk.CTkLabel(
            self,
            text="Teste başlamak için butona tıklayın",
            font=ctk.CTkFont(size=13),
            text_color="#b0b0b0",
        )
        self.status_label.pack(pady=(10, 5))

       
        self.progress_bar = ctk.CTkProgressBar(self, width=460)
        self.progress_bar.set(0)
        self.progress_bar.pack(pady=(0, 20))

        
        self.start_button = ctk.CTkButton(
            self,
            text="TESTİ BAŞLAT",
            font=ctk.CTkFont(size=16, weight="bold"),
            height=50,
            corner_radius=25,
            command=self.start_test_thread,
        )
        self.start_button.pack(pady=10, padx=40, fill="x")

  
    def start_test_thread(self):
        """Butona tıklanınca çağrılır; gerçek işi arka planda başlatır."""
        self.start_button.configure(state="disabled")
        self._reset_ui_before_test()

        test_thread = threading.Thread(target=self.run_speed_test, daemon=True)
        test_thread.start()

    def _reset_ui_before_test(self):
        self.download_value_label.configure(text="-- Mbps")
        self.upload_value_label.configure(text="-- Mbps")
        self.ping_value_label.configure(text="-- ms")
        self.server_value_label.configure(text="--")
        self.progress_bar.set(0)
        self._update_status("Sunucu seçiliyor...")

  
    def run_speed_test(self):
        if speedtest is None:
            self._update_status(
                "Hata: 'speedtest-cli' kütüphanesi bulunamadı. "
                "Lütfen 'pip install speedtest-cli' komutunu çalıştırın."
            )
            self._finish_test(success=False)
            return

        try:
          
            self._update_status("Sunucu seçiliyor...")
            self._set_progress(0.05)
            st = speedtest.Speedtest()
            st.get_servers()

            self._update_status("En iyi sunucu bulunuyor...")
            self._set_progress(0.15)
            best_server = st.get_best_server()

            server_name = best_server.get("name", "Bilinmiyor")
            server_country = best_server.get("country", "")
            server_sponsor = best_server.get("sponsor", "")
            server_text = f"{server_sponsor}\n{server_name}, {server_country}"
            self.after(0, lambda: self.server_value_label.configure(text=server_text))

            
            self._update_status("Ping (gecikme) ölçülüyor...")
            self._set_progress(0.30)
            ping_result = best_server.get("latency", 0.0)
            self.after(
                0,
                lambda: self.ping_value_label.configure(
                    text=f"{ping_result:.0f} ms"
                ),
            )

            
            self._update_status("İndirme testi yapılıyor...")
            self._set_progress(0.50)
            download_speed_bps = st.download()  
            download_mbps = download_speed_bps / 10**6  
            self.after(
                0,
                lambda: self.download_value_label.configure(
                    text=f"{download_mbps:.1f} Mbps"
                ),
            )

            self._update_status("Yükleme testi yapılıyor...")
            self._set_progress(0.80)
            upload_speed_bps = st.upload()  
            upload_mbps = upload_speed_bps / 10**6  
            self.after(
                0,
                lambda: self.upload_value_label.configure(
                    text=f"{upload_mbps:.1f} Mbps"
                ),
            )

           
            self._set_progress(1.0)
            self._update_status("Test Tamamlandı!")
            self._finish_test(success=True)

        except speedtest.ConfigRetrievalError:
            self._update_status(
                "Hata: Speedtest sunucu ayarlarına ulaşılamadı. "
                "İnternet bağlantınızı kontrol edin."
            )
            self._finish_test(success=False)

        except Exception:
           
            self._update_status(
                "Hata: Test tamamlanamadı. İnternet bağlantınızı kontrol edin."
            )
            self._finish_test(success=False)

  
    def _update_status(self, text: str):
        self.after(0, lambda: self.status_label.configure(text=text))

    def _set_progress(self, value: float):
        self.after(0, lambda: self.progress_bar.set(value))

    def _finish_test(self, success: bool):
        def _restore():
            self.start_button.configure(state="normal")
            if not success:
                self.progress_bar.set(0)

        self.after(0, _restore)



if __name__ == "__main__":
    app = SpeedTestApp()
    app.mainloop()
