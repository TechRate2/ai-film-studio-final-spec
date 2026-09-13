# Dự án AI Film Studio: giải thích cho chủ sản phẩm

Ngày đối chiếu: 2026-09-13. Bản hợp đồng hiện tại: **4.5.0** (cập nhật lựa chọn thoại/voice theo ADR-0005). Mốc dưới đây ghi nhận lượt đọc nền trước cập nhật. Mốc đọc: `main@01a7767d57dd0ab78dde4cf25e5fbf1f0ef4c649`, cây Git `e0c7a53d16c1f8cb6781c95bc5c5b462fc892e72`.

Đây là tài liệu giải thích, không phải đặc tả thay thế. Khi có khác biệt, thứ tự thẩm quyền trong AGENTS.md và spec/00 vẫn quyết định. Các khả năng dưới đây là **hành vi phải xây và kiểm chứng**, không phải tính năng đã chạy.

## 1. Repo này thực sự là gì?

Bạn đang sở hữu bản thiết kế để xây một **xưởng làm video do một AI Đạo diễn điều phối**. Người dùng nói ý tưởng, đưa ảnh/video/tài liệu; phần mềm tìm cách sản xuất, cho xem chi phí và kết quả, hỗ trợ sửa và xuất video. Nó không phải một model video mới do bạn huấn luyện.

Hãy hình dung ba bộ phận cùng làm việc:

| Bộ phận | Vai trò | Điều không nên hiểu nhầm |
|---|---|---|
| AI Đạo diễn, sử dụng model suy luận | Hiểu yêu cầu, nghiên cứu, viết ý tưởng, quyết định cách quay/dựng và gọi công cụ | Không tự bảo đảm mọi quyết định đều đúng hoặc phim nào cũng hay |
| Model tạo hình/video/giọng | Thực hiện yêu cầu sản xuất, ban đầu ưu tiên Seedance qua provider phù hợp | Seedance không phải toàn bộ “bộ não”; model có giới hạn thực tế |
| Phần mềm quản lý sản xuất | Lưu dự án, kiểm tra quyền chi tiền, xếp việc, giữ phiên bản, dựng/xuất và phục hồi khi lỗi | Những quy tắc này phải được lập trình và kiểm thử; viết vào prompt chưa đủ |

Có **hai chức năng người dùng độc lập**: Studio tạo video mới; và dịch phụ đề/lồng tiếng trên video có sẵn. Chúng dùng chung hạ tầng, nhưng chức năng thứ hai được xây sau khi Studio vượt cổng phát hành lõi.

## 2. Đã có những tài liệu nào, dùng để làm gì?

Đợt đọc này kiểm kê **266 file được Git theo dõi**, không tính dữ liệu nội bộ của Git. Sau bổ sung hướng dẫn này là 267 file; V4.5.0 thêm một ADR, tổng hiện tại 268 file. Nội dung của toàn bộ tập file được xem xét; các bản JSON fixture lặp lại được đối chiếu bằng bản gốc và phần khác biệt không mất dữ liệu, không tuyên bố đó là đọc lại từng dòng lặp theo nguyên văn. Các đoạn đầu ra bị cắt đã được đọc bù. Hash của 266 file được kiểm tra không đổi trước khi chỉnh sửa.

| Nhóm | Số file tại mốc đọc | Ý nghĩa dễ hiểu |
|---|---:|---|
| File gốc | 6 | Giới thiệu, phiên bản và luật bắt buộc cho người/AI viết code |
| spec | 48 | Sản phẩm phải xử lý thế nào, kể cả khi có lỗi |
| schemas | 45 | Mẫu dữ liệu chính xác để frontend, backend và Agent hiểu cùng một cấu trúc |
| tasks | 49 | 46 nhiệm vụ có số và 3 tài liệu thứ tự/template |
| phases | 8 | Các cổng nghiệm thu trước khi đi tiếp |
| evals | 3 | 33 tình huống Golden, rubric benchmark và 143 trường hợp dữ liệu mẫu hiện tại |
| skills | 39 | 38 thẻ kỹ năng truy xuất chọn lọc và một README |
| knowledge | 10 | Kiến thức làm phim: quyết định, đánh đổi, khi không nên dùng kỹ thuật |
| profiles | 14 | Hồ sơ model/provider/ảnh/giọng và hướng dẫn; gồm 10 file YAML |
| evidence | 11 | Nguồn tham khảo, điều chưa biết và lịch sử audit |
| examples | 4 | Ví dụ áp dụng các hợp đồng |
| prompts | 7 | Cách khởi động và giao việc cho coding agent |
| governance | 11 | Luật thay đổi, nghiệm thu, bàn giao và chương trình kiểm tra tài liệu |
| traceability | 3 | Nối 96 yêu cầu với task, schema, Golden và bằng chứng triển khai |
| docs | 5 | Các quyết định kiến trúc tại mốc đọc; hiện nhóm có 7 file gồm hướng dẫn này và ADR-0005 |
| .github | 3 | Mẫu issue/PR và CI kiểm tra hợp đồng |

**Cả 96 yêu cầu hiện vẫn mang trạng thái NOT_STARTED trong sổ triển khai.** Điều đó đúng với repo đặc tả: chưa có bằng chứng ứng dụng thực hiện chúng. Số file nhiều không có nghĩa đã xây được nhiều phần mềm. Ngược lại, cũng không nên xóa schema/test chỉ để repo nhìn gọn hơn.

## 3. Người dùng sẽ thấy gì?

Màn hình chính là dự án, khung trò chuyện, nút đính kèm ảnh/video/audio/document, tiến độ, bản xem trước, chi phí ước tính và nút Create. Giao diện có tiếng Việt và tiếng Anh. Các lựa chọn model, keyframe, chất lượng, giới hạn chi tiêu và nghiên cứu mở dần khi cần.

Người dùng không phải tự nối một sơ đồ kỹ thuật. Tuy nhiên, việc cần quyết định thật—một yêu cầu không khả thi, một lần sửa phát sinh tiền, một đoạn thoại chưa nghe rõ—vẫn phải được đưa ra rõ ràng. “Tự động” không có nghĩa âm thầm đoán mọi thứ.

## 4. Luồng tạo video mới: từ ý tưởng đến bản xuất

Ví dụ: bạn đưa ảnh túi xách, video tham khảo cách quay và yêu cầu “làm quảng cáo 30 giây, giữ đúng sản phẩm, giọng Việt tự nhiên”.

| Bước | Agent/phần mềm xử lý | Kết quả và điều kiện |
|---|---|---|
| 1. Nhận yêu cầu | Hiểu mục đích, người xem, thời lượng, ngôn ngữ, giới hạn tiền và tài liệu | Thiếu dữ kiện quan trọng thì hỏi đúng chỗ; không bịa giá/công dụng túi |
| 2. Hiểu tài sản | Kiểm tra file, nguồn, quyền; nhóm các góc của cùng sản phẩm; xác định vai trò tham chiếu | Ảnh túi giữ hình dáng túi; video chỉ tham khảo camera không được kéo theo mặt người/bối cảnh |
| 3. Chọn độ sâu | Xem đây là clip độc lập hay câu chuyện/series có nhiều trạng thái cần nhớ | Clip đơn giản không bắt buộc tạo cả Bible, storyboard hoặc nghiên cứu dài |
| 4. Nghiên cứu khi đáng tiền | Dùng kiến thức còn mới trong bộ nhớ; tìm thêm nếu thiếu thông tin ảnh hưởng quyết định | Kết quả web được chắt lọc thành bằng chứng có nguồn, độ mới, độ tin cậy và điểm mâu thuẫn |
| 5. Đạo diễn | Chọn lời hứa với người xem, hook, diễn tiến, bằng chứng, cách diễn/quay/dựng/âm thanh | Mỗi đoạn phải có lý do để người xem tiếp tục; không đồng nhất giữ chân với cắt thật nhanh |
| 6. Chọn cách sản xuất | So sánh dùng clip có sẵn, ảnh có chuyển động, nối tiếp đầu ra trước hoặc tạo video mới | Chọn cách đáp ứng chất lượng với tổng chi phí hợp lý, không chỉ model có đơn giá rẻ |
| 7. Chuẩn bị có chọn lọc | Lấy bộ tham chiếu nhỏ đủ dùng; tạo/lấy keyframe chỉ khi cần | Có ảnh ngoài phù hợp thì tái dùng; không bắt mua ảnh nội bộ |
| 8. Biên dịch yêu cầu | Ý đồ trung lập → UniversalVideoSpec → compiler đúng model → adapter đúng provider | Kiểm tra chức năng, ngôn ngữ, chế độ API và tham số phù hợp trước khi gửi |
| 9. Duyệt và chạy | Ghi quyền chi tiền cho kế hoạch, giữ chỗ ngân sách, gửi các lượt đã cho phép | Mặc định một ứng viên mỗi lượt; cảnh phụ thuộc chỉ chạy sau khi đầu ra cha được chấp nhận |
| 10. Kiểm tra đầu ra | So với ý đồ, sản phẩm, mặt, diễn xuất, liên tục, thoại và lỗi kỹ thuật | Provider báo xong không đồng nghĩa video đạt; lỗi chất lượng không tự sinh lượt trả phí mới |
| 11. Dựng và xuất | Ghép các phiên bản được chấp nhận, cắt, âm thanh, phụ đề theo timeline lưu bền | Kiểm tra hình/tiếng, thời lượng, ngôn ngữ, codec và nguồn trước khi đánh dấu bản cuối |

Đây là quan hệ phụ thuộc, không phải mười một màn hình bắt buộc. Các bước không cần có thể bỏ qua; phần đã đúng được tái dùng.

Căn cứ: spec/01–06, 10–16, 18–21, 29, 31, 33, 40–46 và các task tương ứng trong traceability.

## 5. Nghiên cứu, kiến thức đạo diễn và “bộ não thông minh”

Agent được thiết kế để **tự tìm thông tin khi có ích**: sự thật hiện tại, kiến thức sản phẩm, người xem, phong cách, ngôn ngữ hình ảnh, cách dùng model/provider. Nếu cache đủ mới và đáng tin, không tìm lại. Nếu tìm tiếp ít khả năng cải thiện quyết định, hết ngân sách hoặc đã đủ bằng chứng, phải dừng. Một thông tin quan trọng chưa rõ có thể khiến kế hoạch bị chặn thay vì được đoán.

Kiến thức sáng tạo gồm tâm lý người xem, câu chuyện, diễn xuất/ngầm ý, vị trí nhân vật, hướng nhìn, khung hình, ánh sáng, nhịp dựng, âm thanh và mục đích cảm xúc. Ví dụ: lúc nhân vật nghe một bí mật, giữ phản ứng trong im lặng có thể hiệu quả hơn quay vòng camera hoặc cắt liên tục.

Tham khảo phong cách có nghĩa lấy cơ chế hữu ích—nhịp, cách mở câu hỏi, bố cục, màu, âm thanh—và ghi rõ điều không sao chép. Phong cách không được lấn át sự thật sản phẩm, quyền sử dụng hoặc yêu cầu cứng.

Các thẻ này là hướng dẫn quyết định có thể truy xuất, **không phải một bộ tri thức bảo đảm thay thế mọi chuyên gia điện ảnh**. Sự thông minh thực tế còn phụ thuộc LLM, công cụ, chất lượng nguồn, cách triển khai và đánh giá đầu ra. Bộ nhớ sở thích học từ phản hồi có phạm vi và cho sửa/xóa; không có nghĩa hệ thống tự huấn luyện lại trọng số model.

## 6. Vì sao phim dài và sửa giữa phim không bị mất mạch?

Project Canon là hồ sơ sự thật của dự án. Nó giữ nhân vật, bối cảnh, đồ vật, quan hệ, sự kiện và các câu chuyện chưa giải quyết. Series có thể có 10+ nhân vật quan trọng, nhưng mỗi cảnh chỉ lấy phần cần dùng.

Phần mềm phải phân biệt: sự thật trong thế giới; khán giả biết gì; nhân vật biết, tin, nghi ngờ, hiểu nhầm, che giấu, muốn và sợ gì. Nhân vật chưa nghe bí mật không được tự nhiên hành động như đã biết. Chat không thay thế hồ sơ này.

Không chia mọi cảnh thành 8 hay 15 giây. Một đoạn gọi model có thể chứa nhiều shot dựng; một cảnh có thể cần nhiều đoạn tạo. Agent chọn độ dài đáng tin theo độ phức tạp, chuyển trạng thái, giới hạn route và nhu cầu dựng.

Ví dụ cảnh A kết thúc nhân vật bị thương ở tay trái. Cảnh B phụ thuộc A phải đợi A được chấp nhận, nhận trạng thái quan sát từ A và vẫn dùng tham chiếu gốc làm chuẩn danh tính. A bị từ chối thì B chưa được chạy.

Khi bạn yêu cầu “chậm động tác kiếm, giữ mặt/camera/điểm kết”, hệ thống tải bản cũ cùng yêu cầu nối trước/sau. Nó thử xem chỉnh tốc độ có giữ được thoại và thời gian không; nếu không mới đề xuất tạo video lại, báo tiền. V1 vẫn tồn tại, V2 là bản mới. Tạo bản nháp chưa làm hỏng cảnh sau. Chỉ khi chấp nhận thay đổi không tương thích mới đánh dấu phần phụ thuộc cần xem lại; không tự tạo lại toàn bộ phim.

Căn cứ: spec/07–08, 11–12, 17, 21, 29, 32 và 44.

## 7. Keyframe, Seedance và tiếng Việt

Keyframe là ảnh hướng dẫn một trạng thái hình ảnh quan trọng; **không phải video nào cũng cần**. Có năm đường: tạo ảnh nội bộ; hướng dẫn bạn tạo ngoài rồi tải lên; ảnh bạn có sẵn; khung hình từ video đã chấp nhận; hoặc NONE. NONE nghĩa không có keyframe, không phải tự chọn một provider ảnh khác.

Seedance 2.0 và 2.5 có hồ sơ riêng. Provider như AtlasCloud quyết định endpoint, cách gửi file, quyền tài khoản, giá và chức năng thực sự được mở. Model có một khả năng chưa đủ: provider, tài khoản và chính sách cũng phải cho phép. UNKNOWN không được tự đổi thành “hỗ trợ”. Khi thêm model mới, mở rộng profile/compiler/adapter và kiểm thử; không nhét tên vendor vào bộ não Đạo diễn.

Bốn thứ độc lập: ngôn ngữ giao diện, ngôn ngữ hướng dẫn model, ngôn ngữ thoại và ngôn ngữ phụ đề. Prompt tiếng Anh có thể yêu cầu thoại Việt, nhưng **không biến model nói Việt kém thành nói tốt**.

| Nhu cầu | Hướng xử lý trong thiết kế |
|---|---|
| Native audio đã được chứng minh tốt và được policy cho phép | Có thể dùng trực tiếp, vẫn kiểm tra đầu ra |
| Chọn thoại Việt trong policy ban đầu | Dùng giọng riêng có kiểm chứng hoặc audio nhập; lip-sync thêm là tùy chọn, báo tổng tiền |
| Clip thuyết minh ngoài hình | Có thể dùng voice riêng, không mặc định cần lip-sync |
| Nhân vật lộ miệng nói chính xác | Cần kiểm chứng route đồng bộ hình/tiếng; không chỉ ghép TTS là xong |
| Thoại Anh/Trung với Vietsub | Chỉ dùng khi người dùng đồng ý với lựa chọn nội dung này |

**Lựa chọn mới đã chốt trong V4.5.0:** Studio hiện mặc định đề xuất thoại Trung (Quan thoại) khi dự án mới cần nói nhưng chưa yêu cầu ngôn ngữ nào. Bạn viết mô tả tiếng Việt không tự đổi thoại. Nếu bạn nói rõ “thoại Anh/Việt”, lựa chọn đó thắng mặc định và hiện trong bản xem trước; series giữ ngôn ngữ cũ. Yêu cầu không thoại không bị thêm thoại. Phụ đề mặc định tắt và chọn ngôn ngữ riêng.

Chọn Việt hiện phương án giọng riêng (TTS hoặc audio phù hợp bạn tải lên) cùng chi phí. “Khớp môi” mặc định tắt; chỉ bật khi bạn chọn/yêu cầu rõ và route được kiểm chứng. Nếu để tắt mà có mặt nhân vật đang nói, phải hiểu và chấp nhận giới hạn lồng tiếng thường; không được báo đã khớp môi. Nếu bạn yêu cầu khớp môi nhưng route không đáp ứng, hệ thống báo trước khi chạy. Chọn ngôn ngữ/giọng không tự gọi API có phí; Create duyệt đúng kế hoạch và chi phí đã hiển thị.

Sau khi xong phim Trung/Anh, nút dịch/thêm phụ đề mở một bản nháp dịch riêng từ đúng phiên bản phim đã chấp nhận; không tự mua lượt dịch hay lồng tiếng. Chức năng đó vẫn không sửa môi.

Căn cứ: spec/09, 13–16, 31, 37, 46. Các profile hiện chưa được bật như những route production đã kiểm chứng.

## 8. Luồng dịch phụ đề/lồng tiếng video gốc

Người dùng không cần mua chức năng tạo video để dùng luồng này. Họ đưa video có quyền sử dụng, chọn ngôn ngữ đích, tích phụ đề, lồng tiếng hoặc cả hai.

1. **Nhận diện nguồn:** kiểm tra video, phát hiện tiếng nói/ngôn ngữ theo đoạn, chép lời và xác định người nói. Đoạn không rõ phải giữ trạng thái chưa chắc; giọng trong audio không tự chứng minh người nào trên màn hình đang nói.
2. **Dịch có ngữ cảnh:** giữ tên, số liệu, phủ định, thuật ngữ và cảm xúc. Câu phụ đề và câu đọc có thể khác cách diễn đạt nhưng không khác nghĩa.
3. **Phụ đề:** chia câu dễ đọc, thời điểm, font, màu, vị trí và vùng an toàn. Chỉ làm phụ đề thì không gọi TTS.
4. **Lồng tiếng nếu chọn:** gán giọng theo người nói, dùng giọng được phép hoặc audio nhập; tạo những đoạn cần thiết theo ngân sách đã duyệt. Sao chép giọng thật cần quyền phù hợp.
5. **Căn chỉnh:** đặt audio/phụ đề theo thời gian. Nếu câu quá dài, thử điều chỉnh khoảng nghỉ/tốc độ trong giới hạn; cần đổi câu hay tạo voice mới thì đưa ra đề xuất, không nuốt chữ để ép vừa.
6. **Sửa và kiểm tra một nút:** phát hiện lệch, âm lượng, phụ đề khó đọc, xung đột sau chỉnh tốc độ. Chỉ áp dụng sửa an toàn vào phần không khóa; có hoàn tác. Không tự đổi người nói, nội dung hoặc gọi lại TTS có phí.
7. **Xuất:** file phụ đề rời, video gắn phụ đề, audio hoặc bản ghép theo chế độ; giữ nguồn gốc và lịch sử.

Đổi tốc độ video phải tính lại toàn bộ ánh xạ thời gian liên quan. Đổi tốc độ một đoạn giọng không được âm thầm kéo cả video. Âm nhạc đã trộn với giọng cũ có thể tách không sạch; cần nghe trước và có phương án dùng stem gốc, tắt track hoặc chỉ phụ đề.

**Luồng này không đổi mặt, không tạo video mới bằng AI và không sửa môi.** Nó có thể xuất bản phái sinh bằng ghép tiếng/chèn chữ/chỉnh tốc độ; bản nguồn vẫn được giữ. Khớp thời gian thoại không đồng nghĩa miệng gốc khớp tiếng dịch.

Căn cứ: `spec/47_SOURCE_VIDEO_LOCALIZATION.md`, TASK-044–046, GS29–33, ADR-0002.

## 9. Tiền được tính và bảo vệ thế nào?

Tổng chi phí gồm: LLM và nghiên cứu + nhận dạng/đọc nội dung + ảnh cần tạo + số giây video thực sự sinh + giọng/âm thanh/lip-sync khi có + xử lý/lưu trữ/truyền dữ liệu + các lần sửa người dùng cho phép. Không phải phút video cuối nào cũng tốn cùng tiền.

Một phút có nhiều tài sản tái dùng và thuyết minh thường khác một phút đối thoại cận mặt, nhiều nhân vật, hành động và giữ đồ vật chính xác. Chỉ lấy đơn giá video nhân 60 có thể bỏ sót phần lớn chi phí. Chỉ số kinh tế nên theo dõi là **tổng tiền / số giây đầu ra được chấp nhận**, có tính các lượt thất bại; chưa có mẫu đo thì chưa có số đáng tin.

Create có thể duyệt trước các lượt đầu của cả kế hoạch, tránh hỏi từng shot. Mặc định mỗi lượt một ứng viên. Kết quả xấu không tự gọi lần trả phí khác. Timeout không được gửi lại mù quáng: trước hết tìm xem tác vụ cũ đã được nhận/tính tiền chưa. Hủy không hứa chắc provider hoàn tiền.

“Không có lượt tạo trả phí mới” không đồng nghĩa máy chủ, ASR hoặc LLM miễn phí. Bảng giá public và giá gói thuê bao đối thủ cũng không tự bằng đơn giá API tài khoản của bạn. Repo chưa chứa bảng giá kinh doanh cuối cùng hay bảo đảm lợi nhuận.

## 10. Đối chiếu sản phẩm và tài liệu thực tế

Nguồn dưới đây được mở trực tiếp ngày 2026-09-13. Đây là đối chiếu tài liệu chính chủ, **không phải benchmark chạy tài khoản trả phí, xem và chấm toàn bộ video demo, hoặc điều tra mọi sản phẩm trên thế giới**. Trang quảng cáo là bằng chứng nhà cung cấp công bố tính năng, chưa phải bằng chứng tỷ lệ thành công. Không đủ căn cứ cho phần trăm “giống Topview” hay xếp hạng trí thông minh.

| Nguồn | Nội dung xác nhận trong tài liệu | Hệ quả cho dự án |
|---|---|---|
| [Topview](https://www.topview.ai/) | Agent nhận ý tưởng/script/reference/product URL, lập cảnh, chọn model; Canvas cho sửa shot; có Drama Studio và quản lý tài sản | Ý tưởng Agent đa công đoạn không độc quyền. Cần chứng minh bằng kết quả cùng bài test, không tuyên bố hơn họ chỉ vì spec rộng |
| [LTX Studio](https://ltx.io/studio) | Characters/Objects/Locations, storyboard, timeline, sound design, nhiều điểm bắt đầu | Cách giữ tài sản xuyên cảnh và cho sửa có cơ sở thực tế; không buộc UI mặc định phức tạp như công cụ chuyên nghiệp |
| [ElevenLabs Dubbing Studio](https://elevenlabs.io/docs/eleven-creative/products/dubbing/dubbing-studio) | Fixed duration có thể làm giọng nhanh/chậm bất thường; dynamic có thể lệch thời gian; có lịch sử clip. V1 Studio đang maintenance; v2 không có sửa trong app, API sửa transcript/tạo lại thuộc Enterprise theo trang này | Không mặc định mua dịch vụ dubbing trọn gói là có đủ quyền sửa từng câu. Kiểm tra model, API và entitlement trước khi chọn; giữ editor/state của mình |
| [WhisperX](https://github.com/m-bain/whisperX) | Căn thời gian từ và phân người nói; tự ghi rõ hạn chế overlap, diarization, từ không có trong bộ căn âm và model riêng theo ngôn ngữ | Không hứa timestamp mọi từ hoặc phân vai 100%; giữ vùng chưa rõ, cho sửa và kiểm thử từng ngôn ngữ |
| [VideoLingo](https://github.com/Huanshere/VideoLingo) | Chia phụ đề, thuật ngữ, dịch/phản tư/thích nghi, nhiều TTS; README thừa nhận khó khăn về tốc độ, ngữ điệu và video đa ngôn ngữ | Học kỹ thuật có ích, không sao chép luật “một dòng luôn tốt” hay xóa output/retry thành luật production của mình |
| [AtlasCloud Seedance 2.0](https://www.atlascloud.ai/docs/more-models/bytedance/seedance-2.0-reference-to-video/generateVideo) | Endpoint công bố duration 4–15 hoặc -1; audio reference cần image/video; seed không bảo đảm kết quả hoàn toàn giống | Giới hạn là dữ liệu route có ngày kiểm tra, không phải cách chia mọi phim; reproducibility phải giữ output thật |
| [AtlasCloud Seedance 2.5](https://www.atlascloud.ai/docs/more-models/bytedance/seedance-2.5-reference-to-video/generateVideo) | Công bố duration 4–30 hoặc -1; edit yêu cầu -1/adaptive; prompt có thể kích hoạt sai mode; 4k-esr là nâng từ 1080p, không phải sinh native 4K | Compiler phải đối chiếu ý nghĩa prompt với chế độ và tham số; giữ riêng profile 2.0/2.5, không tự quảng cáo mọi 4K là native |

Chi tiết tiền đáng chú ý trong tài liệu ElevenLabs: tạo dự án qua Dubbing API đã thu tiền trước cho một ngôn ngữ; thêm ngôn ngữ có thể phát sinh phí riêng. Vì vậy một endpoint tên “create project” không mặc nhiên là thao tác miễn phí. Hợp đồng phân loại công cụ theo tác dụng và quyền chi tiền phải được áp dụng ở adapter, kể cả bước chuẩn bị nguồn. Đây là lưu ý tích hợp theo spec/18, 44, 46, 47; chưa chọn ElevenLabs làm phụ thuộc bắt buộc.

Trang Runway Agent được yêu cầu lại nhưng trả HTTP 403 trong lượt này; không tính là nguồn xác minh mới. Nguồn Runway đã lưu trong báo cáo thị trường trước đó vẫn là bằng chứng có ngày lịch sử, không được đổi thành “vừa kiểm chứng”. Các claim native voice, quyền real-person reference, giá và hạn mức của AtlasCloud vẫn phải xác minh trên tài khoản/endpoint thực; việc đọc docs không bật route production.

## 11. Sai sót tìm thấy và xử lý lần này

Không tìm thấy lý do có bằng chứng để thay một Director bằng nhiều bộ não hoặc bỏ các quy tắc an toàn hiện có. Có các sai lệch tài liệu dưới quyền spec cần sửa:

| ID | Phân loại / mức | Vấn đề trước sửa | Sửa nhỏ nhất |
|---|---|---|---|
| U01 | STALE / LOW | Checklist vẫn nói 43 task thay vì 46 | Nối số lượng với manifest và nhắc cổng localization sau lõi |
| U02 | UNDER_SPECIFIED / MEDIUM | Ví dụ prompt tiếng Việt dễ bị xem là yêu cầu API đã được xác minh | Ghi rõ ý đồ minh họa, kiểm chứng ngôn ngữ/route/syntax trước khi gọi |
| U03 | CONFLICT / MEDIUM | Ví dụ sửa kiếm mặc định video, thiếu phân biệt bản nháp và chấp nhận gây stale | Thử retime phù hợp trước; chỉ chấp nhận thay đổi mới làm stale phần phụ thuộc |
| U04 | MISSING / MEDIUM | Chủ sản phẩm thiếu một hướng dẫn tổng thể bằng tiếng Việt | Thêm tài liệu này, không tạo cây spec song song |

U01 dựa vào manifest/order; U02 dựa spec/09,14,31,46; U03 dựa spec/17. Không đổi schema/API/state, không đổi SPEC_LOCK, không đánh dấu task triển khai xong và không chi API. Các lỗi CRITICAL/HIGH ở các audit trước được lưu trong `evidence/AUDIT_ISSUE_MATRIX.csv` và `evidence/FINAL_AUDIT_REPORT.md`; việc sửa chúng là hoàn thành hợp đồng, không chứng nhận code chưa tồn tại.

## 12. Claude/Codex sẽ build theo cách nào?

Dùng `governance/IMPLEMENTATION_HANDOFF.md` và `tasks/00_IMPLEMENTATION_ORDER.md`, không yêu cầu “đọc toàn bộ file mỗi lần rồi tự làm hết”. Phiên đầu xác định repo triển khai, cài hướng dẫn gốc, ghim phiên bản hợp đồng và xác nhận môi trường. Mỗi lượt chọn một task đủ điều kiện, đọc tài liệu liên quan, xem code thật, lập thiếu hụt, làm một lát chức năng hoàn chỉnh và chứng minh từng tiêu chí.

| Giai đoạn | Công việc và bằng chứng cần có |
|---|---|
| 0 | TASK-001 kiểm tra thực tế, không xây app; TASK-002 gắn hợp đồng và quy trình vào repo triển khai |
| 1 | TASK-003–018: dữ liệu, chat, Director, research, reference, sáng tạo, Canon, giọng và diễn xuất; chứng minh quyết định trước video có phí |
| 2 | Luồng Seedance thật với job bền và PaidAttemptGuard trước mọi media có phí; QA, revision, voice, timeline và benchmark |
| 3 | Kiểm tra crash, restart, timeout, hủy, callback, chi phí và phục hồi trên chức năng đã xây |
| 4 | Sở thích, Golden tự động, series/episode tiếp và kiểm tra UI |
| 5 | Kiểm chứng việc thêm route/provider qua profile/compiler/adapter/probe; không kế thừa mù hành vi model |
| 6 | An toàn, quyền tài sản, vận hành, restore và beta lõi tại TASK-043 |
| 7 | TASK-044–046: phụ đề, dubbing, retime, review và xuất trên video gốc; kiểm chứng ngôn ngữ riêng |

Số task là mã định danh, **không phải thứ tự 001→046 máy móc**. TASK-032 và TASK-033 phải qua trước lượt ảnh/video/voice có phí đầu tiên. Kiểm thử một chức năng diễn ra ngay khi xây nó; không đợi đến task Golden mới bắt đầu viết test.

Để bắt đầu còn phải chọn môi trường triển khai, LLM suy luận, công cụ tìm kiếm/đọc media, provider video, voice/ASR phù hợp, database, lưu trữ, worker và dịch vụ vận hành. Đây là quyết định triển khai cần ghi và kiểm chứng, không phải cứ có tài khoản Claude/Codex là ứng dụng có API runtime. Chứng cứ nghiệm thu phải chỉ tới code/test/commit/log thật; PARTIAL được giữ để tiếp tục, không được gọi COMPLETE.

## 13. Kết luận dùng cho quyết định của chủ dự án

Thiết kế hiện đã bao quát cả sáng tạo, sản xuất, sửa cục bộ, tiền, phiên bản, dự án dài, xuất bản và localization riêng. Hướng đúng lúc này là xây và đo các lát chức năng thật theo cổng đã có, không tiếp tục thêm hàng loạt “agent siêu trí tuệ”.

Điều chưa có bằng chứng: phim luôn hay, chất lượng tiếng Việt, giữ mặt/sản phẩm qua nhiều cảnh, độ tin cậy dài hạn, chi phí mỗi phút được chấp nhận, khả năng thao tác API theo tài khoản và chất lượng UX khi chạy thật. Các việc đó không thể giải quyết bằng việc tuyên bố tài liệu hoàn chỉnh 100%.

**READY WITH NON-BLOCKING EMPIRICAL UNKNOWNS** là đánh giá về hợp đồng để bắt đầu triển khai có kiểm soát. Nó không có nghĩa sẵn sàng thu tiền khách hoặc đã vượt Topview/LTX. Bất kỳ route chưa kiểm chứng vẫn phải bị chặn tại runtime theo hợp đồng.
